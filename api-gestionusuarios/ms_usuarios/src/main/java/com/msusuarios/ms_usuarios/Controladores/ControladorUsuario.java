package com.msusuarios.ms_usuarios.Controladores;

import com.msusuarios.ms_usuarios.Modelos.Rol;
import com.msusuarios.ms_usuarios.Modelos.Usuario;
import com.msusuarios.ms_usuarios.Repositorios.RepositorioRol;
import com.msusuarios.ms_usuarios.Repositorios.RepositorioUsuario;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.List;

@RestController
@RequestMapping("usuario")
public class ControladorUsuario {
    @Autowired
    private RepositorioUsuario miRepoUsuario;
    @Autowired
    private RepositorioRol miRepoRol;
    @GetMapping("/listar")
    public List<Usuario> listar() {
        return miRepoUsuario.findAll();
    }
    @PostMapping("/crear")
    public Usuario crear(@RequestBody Usuario datosEntrada) {
        datosEntrada.setContrasena(convertirSHA256(datosEntrada.getContrasena()));
        return miRepoUsuario.save(datosEntrada);
    }
    @PutMapping("/actualizar/{id}")
    public Usuario actualizar(@PathVariable String id,
                           @RequestBody Usuario datosEntrada){
        Usuario datosBusqueda = miRepoUsuario.findById(id).orElse(null);
        datosBusqueda.setNombre(datosEntrada.getNombre());
        datosBusqueda.setCorreo(datosEntrada.getCorreo());
        datosBusqueda.setContrasena(convertirSHA256(datosEntrada.getContrasena()));
        return miRepoUsuario.save(datosBusqueda);
        //return "Usuario " + id + " fue actualizado";
    }
    @PutMapping("/{id}/rol/{idRol}")
    public Usuario asignarRol(@PathVariable String id,
                             @PathVariable String idRol){
        Usuario datosBusqueda = miRepoUsuario.findById(id).orElse(null);
        Rol rolBusqueda = miRepoRol.findById(idRol).orElse(null);
        datosBusqueda.setRol(rolBusqueda);
        return miRepoUsuario.save(datosBusqueda);
        //return "Usuario " + id + " fue actualizado";
    }

    @DeleteMapping("/eliminar/{id}")
    public void eliminar(@PathVariable String id){
        miRepoUsuario.deleteById(id);
       // return "Usuario " + id + " fue eliminado";
    }

    public String convertirSHA256(String password) {
        MessageDigest md = null;
        try {
            md = MessageDigest.getInstance("SHA-256");
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return null;
        }
        byte[] hash = md.digest(password.getBytes());
        StringBuffer sb = new StringBuffer();
        for (byte b : hash) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }

    @PostMapping(value = "/login", consumes = MediaType.APPLICATION_JSON_VALUE)
    public Usuario login(@RequestBody Usuario datosEntrada, HttpServletResponse respHttp) throws IOException {

        String correo = datosEntrada.getCorreo();
        Usuario datosConsulta = miRepoUsuario.searchUserMail(correo);
        if (datosConsulta != null && datosConsulta.getContrasena().equals(convertirSHA256(datosEntrada.getContrasena()))) {
            datosConsulta.setContrasena(null);
            System.out.print(datosConsulta);
            return datosConsulta;
        } else {
            System.out.print("contraseña incorrecta");
            respHttp.sendError(HttpServletResponse.SC_UNAUTHORIZED);
            return null;
        }
    }
}
