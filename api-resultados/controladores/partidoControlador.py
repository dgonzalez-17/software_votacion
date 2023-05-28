from modelos.partido import Partido
from repositorios.repositorioPartido import RepositorioPartido

class PartidoControlador():
    def __init__(self):
        self._repositorio_partido = RepositorioPartido()

    def create(self,datos_entrada):
        _partido = Partido(datos_entrada)
        return self._repositorio_partido.save(_partido)

    def read(self):
        datos_partido = self._repositorio_partido.findAll()
        return datos_partido

    def update(self,id,datos_entrada):
        _partido = Partido(datos_entrada)
        return self._repositorio_partido.update(id,_partido)
        
    def delete(self,id):
        return self._repositorio_partido.delete(id) 