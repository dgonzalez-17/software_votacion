import datetime
import json
import re
from waitress import serve
from flask import Flask, request
from flask_jwt_extended import create_access_token, verify_jwt_in_request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import requests
from flask import jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "grupo-8"
jwt = JWTManager(app)

CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/login', methods=['POST'])
def login():
    datos_entrada = request.get_json()
    configuracion = cargar_configuracion()
    headers = {"Content-Type": "application/json; charset=utf8"}
    respuesta = requests.post(configuracion['url-api-gestusuarios'] + "/usuario/login", json=datos_entrada,
                              headers=headers)
    print(respuesta.status_code)
    if respuesta.status_code == 200:
        tiempo_caducidad_tk = datetime.timedelta(60 * 60 * 24)
        usuario = respuesta.json()
        token = create_access_token(identity=usuario, expires_delta=tiempo_caducidad_tk)
        return {"token": token}
    else:
        return jsonify({"message": "verificar credenciales de acceso"})


@app.before_request
def verificar_peticion():
    print("ejecuci'on callback ...")
    #print("url->",request.url)
    #print("url->", limpiarURL(request.url))
    #print("metodo->", request.method)

    endPoint = limpiarURL(request.path)
    excludedRoutes = ["/login"]
    if excludedRoutes.__contains__(request.path):
        pass
    elif verify_jwt_in_request():
        usuario = get_jwt_identity()
        if usuario["rol"] is not None:
            tienePermiso = validarPermiso(endPoint, request.method, usuario["rol"]["_id"])
            if not tienePermiso:
                return jsonify({"message": "Permission denied"}), 401
        else:
            return jsonify({"message": "Permission denied"}), 401


def limpiarURL(url):
    partes = url.split("/")
    for laParte in partes:
        if re.search('\\d', laParte):
            url = url.replace(laParte, "?")
    return url


def validarPermiso(endPoint, metodo, idRol):
    url = datos_configuracion["url-api-gestusuarios"] + "/rolpermiso/" + str(idRol)
    print(url,endPoint,metodo, idRol)
    tienePermiso = False
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = {
        "url": endPoint,
        "metodo": metodo
    }
    response = requests.post(url, json=body, headers=headers)

    try:
        data = response.json()
        print(data)
        if ("_id" in data or "id" in data):
            tienePermiso = True
            print(tienePermiso)
    except:
        pass
    print(tienePermiso)
    return tienePermiso



##-------FUNCIONES DE CONSULTAS-------------##
#----BACKEND GESTUSUARIOS#
#usuario#
@app.route('/usuario', methods=["GET"])
def listar_usuario():
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-gestusuarios"] + "/usuario/listar"
    respuesta = requests.get(url, headers=headers)
    return jsonify(respuesta.json())
@app.route('/usuario', methods=["POST"])
def crear_usuario():
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-gestusuarios"] + "/usuario/crear"
    respuesta = requests.post(url, json=datosEntrada, headers=headers)
    return jsonify(respuesta.json())
@app.route('/usuario/<string:id>', methods=["PUT"])
def modificar_usuario(id):
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-gestusuarios"] + "/usuario/actualizar/"+id
    respuesta = requests.put(url, headers=headers, json=datosEntrada)
    return jsonify(respuesta.json())
@app.route('/usuario/<string:id>/<string:idRol>', methods=["PUT"])
def asignar_rol_usuario(id, idRol):
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-gestusuarios"] + "/usuario/"+id+"/rol/"+idRol
    respuesta = requests.put(url, headers=headers)
    return jsonify(respuesta.json())
@app.route('/usuario/<string:id>', methods=["DELETE"])
def eliminar_usuario(id):
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-gestusuarios"] + "/usuario/eliminar/"+id
    respuesta = requests.delete(url, headers=headers)
    return {"mensaje": "usuario con el id " + id + " eliminado"}

#ROL#
@app.route('/rol', methods=["GET"])
def listar_rol():
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-gestusuarios"] + "/rol/listar"
    respuesta = requests.get(url, headers=headers)
    return jsonify(respuesta.json())
@app.route('/rol', methods=["POST"])
def crear_rol():
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-gestusuarios"] + "/rol/crear"
    respuesta = requests.post(url, json=datosEntrada, headers=headers)
    return jsonify(respuesta.json())
@app.route('/rol/<string:id>', methods=["PUT"])
def modificar_rol(id):
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-gestusuarios"] + "/rol/actualizar/"+id
    respuesta = requests.put(url, headers=headers, json=datosEntrada)
    return jsonify(respuesta.json())
@app.route('/rol/<string:id>', methods=["DELETE"])
def eliminar_rol(id):
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-gestusuarios"] + "/rol/eliminar/"+id
    respuesta = requests.delete(url, headers=headers)
    return {"mensaje": "Rol con el id " + id + " eliminado"}
#PERMISO#
@app.route('/permiso', methods=["GET"])
def listar_permiso():
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-gestusuarios"] + "/permiso/listar"
    respuesta = requests.get(url, headers=headers)
    return jsonify(respuesta.json())
@app.route('/permiso', methods=["POST"])
def crear_permiso():
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-gestusuarios"] + "/permiso/crear"
    respuesta = requests.post(url, json=datosEntrada, headers=headers)
    return jsonify(respuesta.json())
@app.route('/permiso/<string:id>', methods=["PUT"])
def modificar_permiso(id):
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-gestusuarios"] + "/permiso/actualizar/"+id
    respuesta = requests.put(url, headers=headers, json=datosEntrada)
    return jsonify(respuesta.json())
@app.route('/permiso/<string:id>', methods=["DELETE"])
def eliminar_permiso(id):
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-gestusuarios"] + "/permiso/eliminar/"+id
    respuesta = requests.delete(url, headers=headers)
    return {"mensaje": "Permiso con el id " + id + " eliminado"}

#ROLPERMISO#
@app.route('/rolpermiso', methods=["GET"])
def listar_rolpermiso():
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-gestusuarios"] + "/rolpermiso/listar"
    respuesta = requests.get(url, headers=headers)
    return jsonify(respuesta.json())
@app.route('/rolpermiso/<string:idRol>/<string:idPermiso>', methods=["POST"])
def crear_rolpermiso(idRol, idPermiso):
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-gestusuarios"] + "/rolpermiso/"+idRol+"/"+idPermiso
    respuesta = requests.post(url, headers=headers)
    return jsonify(respuesta.json())
@app.route('/rolpermiso/<string:idRolPermiso>/<string:idRol>/<string:idPermiso>', methods=["PUT"])
def modificar_rolpermiso(idRolPermiso, idRol, idPermiso):
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-gestusuarios"] + "/rolpermiso/"+idRolPermiso+\
          "/"+idRol+"/"+idPermiso
    respuesta = requests.put(url, headers=headers)
    return respuesta.json()
@app.route('/rolpermiso/<string:id>', methods=["DELETE"])
def eliminar_rolpermiso(id):
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-gestusuarios"] + "/rolpermiso/eliminar/"+id
    respuesta = requests.delete(url, headers=headers)
    return {"mensaje": "RolPermiso con el id " + id + " eliminado"}


#--------BACKEND RESULTADOS----------#
#MESA#
@app.route('/mesa', methods=["GET"])
def listar_mesa():
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-resultados"] + "/mesa/listar"
    respuesta = requests.get(url, headers=headers)
    return jsonify(respuesta.json())
@app.route('/mesa', methods=["POST"])
def crear_mesa():
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-resultados"] + "/mesa/crear"
    respuesta = requests.post(url, json=datosEntrada, headers=headers)
    return jsonify(respuesta.json())
@app.route('/mesa/<string:id>', methods=["PUT"])
def modificar_mesa(id):
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-resultados"] + "/mesa/"+id
    respuesta = requests.put(url, headers=headers, json=datosEntrada)
    return respuesta.json()
@app.route('/mesa/<string:id>', methods=["DELETE"])
def eliminar_mesa(id):
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-resultados"] + "/mesa/"+id
    respuesta = requests.delete(url, headers=headers)
    return jsonify(respuesta.json())
#CANDIDATO
@app.route('/candidato', methods=["GET"])
def listar_candidato():
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-resultados"] + "/candidato/listar"
    respuesta = requests.get(url, headers=headers)
    return jsonify(respuesta.json())
@app.route('/candidato', methods=["POST"])
def crear_candidato():
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-resultados"] + "/candidato/crear"
    respuesta = requests.post(url, json=datosEntrada, headers=headers)
    return jsonify(respuesta.json())
@app.route('/candidato/<string:id>', methods=["PUT"])
def modificar_candidato(id):
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-resultados"] + "/candidato/"+id
    respuesta = requests.put(url, headers=headers, json=datosEntrada)
    return respuesta.json()
@app.route('/candidato/<string:id>/<string:idPartido>', methods=["PUT"])
def asignar_partido_candidato(id, idPartido):
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-resultados"] + "/candidato/"+id+"/partido/"+idPartido
    respuesta = requests.put(url, headers=headers)
    return jsonify(respuesta.json())
@app.route('/candidato/<string:id>', methods=["DELETE"])
def eliminar_candidato(id):
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-resultados"] + "/candidato/"+id
    respuesta = requests.delete(url, headers=headers)
    return jsonify(respuesta.json())
#PARTIDO
@app.route('/partido', methods=["GET"])
def listar_partido():
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-resultados"] + "/partido/listar"
    respuesta = requests.get(url, headers=headers)
    return jsonify(respuesta.json())
@app.route('/partido', methods=["POST"])
def crear_partido():
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-resultados"] + "/partido/crear"
    respuesta = requests.post(url, json=datosEntrada, headers=headers)
    return jsonify(respuesta.json())
@app.route('/partido/<string:id>', methods=["PUT"])
def modificar_partido(id):
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-resultados"] + "/partido/"+id
    respuesta = requests.put(url, headers=headers, json=datosEntrada)
    return respuesta.json()
@app.route('/partido/<string:id>', methods=["DELETE"])
def eliminar_partido(id):
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-resultados"] + "/partido/"+id
    respuesta = requests.delete(url, headers=headers)
    return jsonify(respuesta.json())
#RESULTADO
@app.route('/resultado', methods=["GET"])
def listar_resultado():
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-resultados"] + "/resultado/listar"
    respuesta = requests.get(url, headers=headers)
    return jsonify(respuesta.json())
@app.route('/resultado/<string:id>', methods=["GET"])
def listar_un_resultado(id):
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-resultados"] + "/candidato/listar/"+id
    respuesta = requests.get(url, headers=headers)
    return jsonify(respuesta.json())
@app.route('/resultado/<string:idCandidato>/<string:idMesa>', methods=["POST"])
def crear_resultado(idCandidato, idMesa):
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-resultados"] + "/resultado/candidato/"\
          +idCandidato+"/mesa/"+idMesa
    respuesta = requests.post(url, json=datosEntrada, headers=headers)
    return jsonify(respuesta.json())
@app.route('/resultado/<string:id>/<string:idCandidato>/<string:idMesa>', methods=["PUT"])
def modificar_resultado(id, idCandidato, idMesa):
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-resultados"] + "/resultado/"+id+"/candidato/"\
          +idCandidato+"/mesa/"+idMesa
    respuesta = requests.put(url, headers=headers, json=datosEntrada)
    return respuesta.json()
@app.route('/resultado/<string:id>', methods=["DELETE"])
def eliminar_resultado(id):
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-resultados"] + "/resultado/"+id
    respuesta = requests.delete(url, headers=headers)
    return jsonify(respuesta.json())
#REPORTE
@app.route('/reporte/totalvotos', methods=["GET"])
def listar_reportes():
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-resultados"] + "/reporte/totalvotos"
    respuesta = requests.get(url, headers=headers)
    return jsonify(respuesta.json())
@app.route('/reporte/votosmesa', methods=["GET"])
def listar_reportes_mesa():
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-resultados"] + "/reporte/totalvotosmesa"
    respuesta = requests.get(url, headers=headers)
    return jsonify(respuesta.json())
@app.route('/reporte/<string:id>', methods=["GET"])
def listar_un_reporte(id):
    headers = {"Content-Type": "application/json; charset=utf8"}
    url = datos_configuracion["url-api-resultados"] + "/reporte/"+id
    respuesta = requests.get(url, headers=headers)
    return jsonify(respuesta.json())

#-----------------------------------------------------------
@app.route('/')
def hello_world():
    return 'API GATEWAY...'


# --------------CONFIGURACION --------------------------------

def cargar_configuracion():
    with open("config.json") as archivo:
        datos_configuracion = json.load(archivo)
    return datos_configuracion


if __name__ == '__main__':
    datos_configuracion = cargar_configuracion()
    print("Servidor gateway corriendo...\n",
          "http://" + datos_configuracion["url-api-gateway"] + ":" + datos_configuracion["puerto-api-gateway"])
    serve(app, host=datos_configuracion["url-api-gateway"], port=datos_configuracion["puerto-api-gateway"])
