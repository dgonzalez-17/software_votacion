from flask import Flask
from flask import request
from flask import jsonify
from waitress import serve 
import json
from controladores.mesaControlador import MesaControlador
from controladores.candidatoControlador import CandidatoControlador
from controladores.partidoControlador import PartidoControlador
from controladores.resultadoControlador import ResultadoControlador
from flask_cors import CORS


ms_resultados = Flask(__name__)

CORS(ms_resultados, resources={r"/*": {"origins": "*"}})

#---------------- LLAMADO CONTROLADORES ------------------------
_controlador_mesa = MesaControlador()
_controlador_candidato = CandidatoControlador()
_controlador_partido = PartidoControlador()
_controlador_resultado = ResultadoControlador()

# --------------PATHS MESA --------------------------------
#POST
@ms_resultados.route('/mesa/crear',methods=['POST'])
def crear_mesa():
    datos_entrada = request.get_json()
    datos_salida = _controlador_mesa.create(datos_entrada)
    return jsonify(datos_salida)
#GET
@ms_resultados.route('/mesa/listar',methods=['GET'])
def listar_mesa():
    datos_salida = _controlador_mesa.read()
    return jsonify(datos_salida)

#PUT
@ms_resultados.route('/mesa/<string:id>',methods=['PUT'])
def actualizar_mesa(id):
    datos_entrada = request.get_json()
    datos_salida = _controlador_mesa.update(id,datos_entrada)
    print (jsonify(datos_salida))
    return jsonify(datos_salida)

    
#DELETE
@ms_resultados.route('/mesa/<string:id>',methods=['DELETE'])
def eliminar_mesa(id):
    datos_salida = _controlador_mesa.delete(id)
    return jsonify(datos_salida)

# --------------PATHS CANDIDATO --------------------------------
#POST
@ms_resultados.route('/candidato/crear',methods=['POST'])
def crear_candidato():
    datos_entrada = request.get_json()
    datos_salida =_controlador_candidato.create(datos_entrada)
    return jsonify(datos_salida)
#GET
@ms_resultados.route('/candidato/listar',methods=['GET'])
def listar_candidato():
    datos_salida =_controlador_candidato.read()
    return jsonify(datos_salida)

#PUT
@ms_resultados.route('/candidato/<string:id>',methods=['PUT'])
def actualizar_candidato(id):
    datos_entrada = request.get_json()
    datos_salida = _controlador_candidato.update(id,datos_entrada)
    return jsonify(datos_salida)
    
#DELETE
@ms_resultados.route('/candidato/<string:id>',methods=['DELETE'])
def eliminar_candidato(id):
    datos_salida = _controlador_candidato.delete(id)
    return jsonify(datos_salida)

#ASIGNAR_PARTIDO
@ms_resultados.route('/candidato/<string:id>/partido/<string:id_partido>',methods=['PUT'])
def asignar_partido_cand(id,id_partido):
    datos_salida = _controlador_candidato.asignarPartido(id,id_partido)
    return jsonify(datos_salida)

# --------------PATHS PARTIDO --------------------------------
#POST
@ms_resultados.route('/partido/crear',methods=['POST'])
def crear_partido():
    datos_entrada = request.get_json()
    datos_salida =_controlador_partido.create(datos_entrada)
    return jsonify(datos_salida)
#GET
@ms_resultados.route('/partido/listar',methods=['GET'])
def listar_partido():
    datos_salida =_controlador_partido.read()
    return jsonify(datos_salida)

#PUT
@ms_resultados.route('/partido/<string:id>',methods=['PUT'])
def actualizar_partido(id):
    datos_entrada = request.get_json()
    datos_salida = _controlador_partido.update(id,datos_entrada)
    return jsonify(datos_salida)
    
#DELETE
@ms_resultados.route('/partido/<string:id>',methods=['DELETE'])
def eliminar_partido(id):
    datos_salida = _controlador_partido.delete(id)
    return jsonify(datos_salida)

# --------------PATHS RESULTADO --------------------------------
#POST
@ms_resultados.route('/resultado/candidato/<string:id_candidato>/mesa/<string:id_mesa>',methods=['POST'])
def crear_resultado(id_candidato,id_mesa):
    datos_entrada = request.get_json()
    datos_salida = _controlador_resultado.create(datos_entrada,id_candidato,id_mesa)
    return jsonify(datos_salida)
#GET-ALL
@ms_resultados.route('/resultado/listar',methods=['GET'])
def listar_resultados():
    datos_salida = _controlador_resultado.index()
    return jsonify(datos_salida)

#GETBYID
@ms_resultados.route('/resultado/listar/<string:id>',methods=['GET'])    
def listar_resultado(id):
    datos_salida = _controlador_resultado.read(id)
    return jsonify(datos_salida)

#PUT
@ms_resultados.route('/resultado/<string:id_resultado>/candidato/<string:id_candidato>/mesa/<string:id_mesa>',methods=['PUT'])
def actualizar_resultado(id_resultado,id_candidato,id_mesa):
    datos_entrada = request.get_json()
    datos_salida = _controlador_resultado.update(id_resultado,datos_entrada,id_candidato,id_mesa)
    return jsonify(datos_salida)
    
#DELETE
@ms_resultados.route('/resultado/<string:id>',methods=['DELETE'])
def eliminar_resultado(id):
    datos_salida = _controlador_resultado.delete(id)
    return jsonify(datos_salida)

#OBTENER REPORTE DE VOTOS GENERALES
@ms_resultados.route('/reporte/totalvotos',methods=['GET'])
def obtener_resultado():
    datos_salida = _controlador_resultado.getCandidatesTotal()
    return jsonify(datos_salida)

#OBTENER RESULTADOS DE VOTOS POR MESA
@ms_resultados.route('/reporte/<string:id_mesa>',methods=['GET'])
def obtener_resultado_mesa(id_mesa):
    datos_salida = _controlador_resultado.getCandidatesbyTables(id_mesa)
    return jsonify(datos_salida)

#OBTENER RESULTADOS DE VOTOS EN MESA DE MENOR A MAYOR
@ms_resultados.route('/reporte/totalvotosmesa',methods=['GET'])
def obtener_resultado_por_mesas():
    datos_salida = _controlador_resultado.getMostVotesTables()
    return jsonify(datos_salida)



# --------------CONFIGURACION --------------------------------

def cargar_configuracion():
    with open("config.json") as archivo:
        datos_configuracion = json.load(archivo)
    return datos_configuracion

if __name__ == '__main__':  
    datos_configuracion = cargar_configuracion()
    print("Servidor corriendo...\n","http://"+datos_configuracion["servidor"]+":"+datos_configuracion["puerto"])
    serve(ms_resultados, host=datos_configuracion["servidor"], port=datos_configuracion["puerto"])

