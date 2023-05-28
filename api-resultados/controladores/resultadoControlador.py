from modelos.resultado import Resultado
from modelos.candidato import Candidato
from modelos.mesa import Mesa
from repositorios.repositorioResultado import RepositorioResultado
from repositorios.repositorioCandidato import RepositorioCandidato
from repositorios.repositorioMesa import RepositorioMesa

class ResultadoControlador():
    def __init__(self):
        self._repositorio_resultado = RepositorioResultado()
        self._repositorio_candidato = RepositorioCandidato()
        self._repositorio_mesa = RepositorioMesa()
    
    def index(self):
        return self._repositorio_resultado.findAll()

    def create(self,datos_entrada,id_candidato,id_mesa):
        resultado = Resultado(datos_entrada)
        candidato = Candidato(self._repositorio_candidato.findById(id_candidato))
        mesa = Mesa(self._repositorio_mesa.findById(id_mesa))
        resultado.candidato = candidato
        resultado.mesa = mesa 
        return self._repositorio_resultado.save(resultado)

    def read(self,id):
        resultado = Resultado(self._repositorio_resultado.findById(id))
        return resultado.__dict__

    def update(self,id,datos_entrada,id_candidato,id_mesa):
        resultado = Resultado(self._repositorio_resultado.findById(id))
        resultado.cedula = datos_entrada["cedula"]
        resultado.nombre = datos_entrada["nombre"]
        candidato = Candidato(self._repositorio_candidato.findById(id_candidato))
        mesa = Mesa(self._repositorio_mesa.findById(id_mesa))
        resultado.candidato = candidato
        resultado.mesa = mesa
        return self._repositorio_resultado.save(resultado)
        
    def delete(self,id):
        return self._repositorio_resultado.delete(id) 

    def getCandidatesTotal(self):
        return self._repositorio_resultado.getCountGeneralCandidates()

    def getCandidatesbyTables(self,id_mesa):
        return self._repositorio_resultado.getCountTableCandidates(id_mesa)

    def getMostVotesTables(self): 
        return self._repositorio_resultado.getCountMostVotesTables()
    
    def mostVotesMatches(self):
        votos = self._repositorio_resultado.getCountGeneralCandidates()
        for voto in votos: 
            print(voto)