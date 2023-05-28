import { EventEmitter, Injectable, Output } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Candidato } from '../models/candidato.model';
import { environment } from '../../environments/environment';
import { debugOutputAstAsTypeScript } from '@angular/compiler';


@Injectable({
  providedIn: 'root'
})
export class CandidatoService {

  @Output() disparadorEdit: EventEmitter<Candidato> = new EventEmitter(); 

  constructor(private http: HttpClient) {
}
  consultarCandidatos(): Observable<Candidato[]> { 
    return this.http.get<Candidato[]>(environment.url_api_gateway +'/candidato')
  }


  crearCandidos(datos: Candidato): Observable<Candidato>{
    return this.http.post<Candidato>(environment.url_api_gateway +'/candidato', datos)
  }

  eliminarCandidato(id:string){
    return this.http.delete<Candidato>(environment.url_api_gateway +'/candidato/'+id);
  }
  editarCandidato(id:string, candidato: Candidato){
    return this.http.put<Candidato>(environment.url_api_gateway +'/candidato/'+id, candidato);
  }
}
