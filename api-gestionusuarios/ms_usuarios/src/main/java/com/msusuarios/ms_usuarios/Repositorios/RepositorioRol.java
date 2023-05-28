package com.msusuarios.ms_usuarios.Repositorios;

import com.msusuarios.ms_usuarios.Modelos.Rol;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioRol extends MongoRepository<Rol,String> {

}
