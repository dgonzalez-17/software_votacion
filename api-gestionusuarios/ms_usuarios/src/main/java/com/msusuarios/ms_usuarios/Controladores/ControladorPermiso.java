package com.msusuarios.ms_usuarios.Controladores;

import com.msusuarios.ms_usuarios.Modelos.Permiso;
import com.msusuarios.ms_usuarios.Repositorios.RepositorioPermiso;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/permiso")
public class ControladorPermiso {
    @Autowired
    private RepositorioPermiso miRepoPermiso;
    @GetMapping("/listar")
    public List<Permiso> listar() {
        return miRepoPermiso.findAll();
    }
    @PostMapping("/crear")
    public Permiso crear(@RequestBody Permiso datosEntrada) {
        return miRepoPermiso.save(datosEntrada);
    }
    @PutMapping("/actualizar/{id}")
    public Permiso actualizar(@PathVariable String id,
                             @RequestBody Permiso datosEntrada){
        Permiso datosBusqueda = miRepoPermiso.findById(id).orElse(null);
        datosBusqueda.setUrl(datosEntrada.getUrl());
        datosBusqueda.setMetodo(datosEntrada.getMetodo());
        return miRepoPermiso.save(datosBusqueda);
        //return "Permiso " + id + " fue actualizado";
    }
    @DeleteMapping("/eliminar/{id}")
    public void eliminar(@PathVariable String id){
        miRepoPermiso.deleteById(id);
        // return "Permiso " + id + " fue eliminado";
    }

}
