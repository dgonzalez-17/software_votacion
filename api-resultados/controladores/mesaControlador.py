from modelos.mesa import Mesa
from repositorios.repositorioMesa import RepositorioMesa

class MesaControlador():
    def __init__(self):
        self._repositorio_mesa = RepositorioMesa()

    def create(self,datos_entrada):
        _mesa = Mesa(datos_entrada)
        return self._repositorio_mesa.save(_mesa)

    def read(self):
        datos_mesa = self._repositorio_mesa.findAll()
        return datos_mesa

    def update(self,id,datos_entrada):
        _mesa = Mesa(datos_entrada)
        return self._repositorio_mesa.update(id,_mesa)
        
    def delete(self,id):
        return self._repositorio_mesa.delete(id) 