package com.msusuarios.ms_usuarios.Controladores;

import com.msusuarios.ms_usuarios.Modelos.Rol;
import com.msusuarios.ms_usuarios.Repositorios.RepositorioRol;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/rol")
public class ControladorRol {
    @Autowired
    private RepositorioRol miRepoRol;
    @GetMapping("/listar")
    public List<Rol> listar() {
        return miRepoRol.findAll();
    }
    @PostMapping("/crear")
    public Rol crear(@RequestBody Rol datosEntrada) {
        return miRepoRol.save(datosEntrada);
    }
    @PutMapping("/actualizar/{id}")
    public Rol actualizar(@PathVariable String id,
                             @RequestBody Rol datosEntrada){
        Rol datosBusqueda = miRepoRol.findById(id).orElse(null);
        datosBusqueda.setNombre(datosEntrada.getNombre());
        datosBusqueda.setDescripcion(datosEntrada.getDescripcion());
        return miRepoRol.save(datosBusqueda);
       // return "Rol " + id + " fue actualizado";
    }
    @DeleteMapping("/eliminar/{id}")
    public void eliminar(@PathVariable String id){
        miRepoRol.deleteById(id);
        //return "Rol " + id + " fue eliminado";
    }


}
