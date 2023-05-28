package com.msusuarios.ms_usuarios.Controladores;

import com.msusuarios.ms_usuarios.Modelos.Permiso;
import com.msusuarios.ms_usuarios.Modelos.Rol;
import com.msusuarios.ms_usuarios.Modelos.RolPermiso;
import com.msusuarios.ms_usuarios.Repositorios.RepositorioPermiso;
import com.msusuarios.ms_usuarios.Repositorios.RepositorioRol;
import com.msusuarios.ms_usuarios.Repositorios.RepositorioRolPermiso;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

@RestController
@RequestMapping("/rolpermiso")
public class ControladorRolPermiso {
    @Autowired
    RepositorioRolPermiso miRepoRolPermiso;
    @Autowired
    RepositorioRol miRepoRol;
    @Autowired
    RepositorioPermiso miRepoPermiso;
    @GetMapping("/listar")
    public List<RolPermiso> listar(){
        return miRepoRolPermiso.findAll();
    }

    @PostMapping("/{idrol}/{idpermiso}")
    public RolPermiso crear(@PathVariable String idrol,
                            @PathVariable String idpermiso){
        Rol rolBusqueda = miRepoRol.findById(idrol).orElse(null);
        Permiso permisoBusqueda = miRepoPermiso.findById(idpermiso).orElse(null);
        RolPermiso rolPermiso = new RolPermiso(rolBusqueda,permisoBusqueda);
        return miRepoRolPermiso.save(rolPermiso);
    }
    @PutMapping("/{idrolpermiso}/{idrol}/{idpermiso}")
    public RolPermiso actualizar(@PathVariable String idrolpermiso,
                           @PathVariable String idrol,
                           @PathVariable String idpermiso){
        RolPermiso rolPermiso = miRepoRolPermiso.findById(idrolpermiso).orElse(null);
        Rol rolBusqueda = miRepoRol.findById(idrol).orElse(null);
        Permiso permisoBusqueda = miRepoPermiso.findById(idpermiso).orElse(null);
        rolPermiso.setRol(rolBusqueda);
        rolPermiso.setPermiso(permisoBusqueda);
        return miRepoRolPermiso.save(rolPermiso);
        //return "El RolPermiso " + idrolpermiso + " se ha actualizado";
    }
    @DeleteMapping("/eliminar/{id}")
    public String eliminar(@PathVariable String id){
        miRepoRolPermiso.deleteById(id);
        return "El RolPermiso " + id + " se ha eliminado";
    }

    @PostMapping("/{idRol}")
    public RolPermiso obtenerPermiso(@PathVariable String idRol,
                                     @RequestBody Permiso permisoEntrada,
                                     HttpServletResponse httpResp) throws IOException {
        //Rol rolConsulta = miRepoRol.findById(idRol).orElse(null);
        Permiso permisoConsulta = miRepoPermiso.consultarPermiso(permisoEntrada.getUrl(), permisoEntrada.getMetodo());

        if (permisoConsulta != null){
            return miRepoRolPermiso.consultarRolPermiso(idRol,
                    permisoConsulta.get_id());
        } else {
            httpResp.sendError(HttpServletResponse.SC_UNAUTHORIZED);
            return null;
        }


    }

}

