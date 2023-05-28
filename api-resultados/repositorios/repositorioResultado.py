from modelos.resultado import Resultado
from repositorios.interfazRepositorio import InterfazRepositorio
from bson import ObjectId

class RepositorioResultado(InterfazRepositorio[Resultado]):
    def getCountGeneralCandidates(self):
        Query =    [  {
                            '$group': {
                                '_id': '$candidato', 
                                'votos totales': {
                                    '$count': {}
                                }
                            }
                        }, {
                            '$sort': {
                                'votos totales': -1
    
                            }
                        }] 
        return self.queryAggregation(Query)

    def getCountTableCandidates(self,id_mesa):
        Query = {'$match':{'mesa.$id':ObjectId(id_mesa)}}
        Query2 = { '$group': {
                        '_id': '$candidato',
                        'votos totales':{
                            '$count':{
                            }
                        }
                        }
            }
        Query3 =  {'$sort': {'votos totales': -1}}
        pipeline = [Query,Query2,Query3] 
        return self.queryAggregation(pipeline)
    
    def getCountMostVotesTables(self):
        Query = [{
                    '$group': {
                        '_id': '$mesa', 
                        'votos totales': {
                            '$count': {}
                        }
                    }
                }, {
                    '$sort': {
                        'votos totales': 1
                    }
                }
            ]
        return self.queryAggregation(Query)