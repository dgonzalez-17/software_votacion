export class Candidato {
    _id?:string;
    nombre?:string;
    cedula?:string;
    resolucion?:string;

    constructor(id?:string, nombre?:string){
        this._id = id;
        this.nombre = nombre;
    }

}

