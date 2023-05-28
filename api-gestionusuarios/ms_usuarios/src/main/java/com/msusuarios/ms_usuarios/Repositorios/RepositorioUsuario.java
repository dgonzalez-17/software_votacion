package com.msusuarios.ms_usuarios.Repositorios;

import com.msusuarios.ms_usuarios.Modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface RepositorioUsuario extends MongoRepository<Usuario,String> {

    @Query("{'correo': ?0}")
    public Usuario searchUserMail(String correo);
}

