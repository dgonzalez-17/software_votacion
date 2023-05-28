from modelos.candidato import Candidato
from repositorios.repositorioCandidato import RepositorioCandidato
from repositorios.repositorioPartido import RepositorioPartido
from modelos.partido import Partido
import pymongo 

class CandidatoControlador():
    def __init__(self):
        self._repositorio_candidato = RepositorioCandidato()
        self._repositorio_partido = RepositorioPartido()
    
    def asignarPartido(self,id,id_partido):
        candidato_actual = Candidato(self._repositorio_candidato.findById(id))
        partido_actual = Partido(self._repositorio_partido.findById(id_partido))
        candidato_actual.partido = partido_actual
        return self._repositorio_candidato.save(candidato_actual)

    def create(self,datos_entrada):
        _candidato = Candidato(datos_entrada)
        return self._repositorio_candidato.save(_candidato)

    def read(self):
        datos_candidato = self._repositorio_candidato.findAll()
        return datos_candidato

    def update(self,id,datos_entrada):
        _candidato = Candidato(datos_entrada)
        return self._repositorio_candidato.update(id,_candidato)
        
    def delete(self,id):
        return self._repositorio_candidato.delete(id) 

