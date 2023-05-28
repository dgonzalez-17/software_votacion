package com.msusuarios.ms_usuarios.Repositorios;

import com.msusuarios.ms_usuarios.Modelos.RolPermiso;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface RepositorioRolPermiso extends MongoRepository<RolPermiso,String> {
    @Query("{\"rol.$id\": ObjectId(?0),\"permiso.$id\": ObjectId(?1)}")
    public RolPermiso consultarRolPermiso(String idRol, String idPermiso);
}
