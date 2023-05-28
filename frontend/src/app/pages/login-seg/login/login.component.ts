import { HttpHeaders } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import Swal from 'sweetalert2';
import { environment } from '../../../../environments/environment';
import { Usuario } from '../../../models/usuario.model';
import { SeguridadService } from '../../../services/seguridad.service';
import { Router } from '@angular/router';

@Component({
  selector: 'ngx-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  correo:string;
  contrasena:string;
  alertaActiva = false;

  constructor(private servicioSeguridad: SeguridadService, private router: Router) { }

  login():void {
    let elUsuario: Usuario = {
        correo: this.correo,
        contrasena: this.contrasena
    }
    this.servicioSeguridad.login(elUsuario).subscribe(
      data=>{
      this.router.navigate(['pages/candidatos/read']);
      this.servicioSeguridad.guardarDatosSesion(data);
    },
      error=>{
    Swal.fire({
      title: 'Error, verificar los datos',
      text: error["error"]["message"],
      icon:"error",
      timer:3000
    });
    this.alertaActiva = true
  }
    );
  }



  ngOnInit(): void {
  }


  /*

  login(correo:string, password:string){
    let usuario = {
      "correo":correo,
      "contrasena":password,
    }
   
    fetch(environment.url_api_gateway+"/login",
    {method:"POST", body: JSON.stringify(usuario), headers: {'Content-Type': 'application/json'}})
    .then(reponse => reponse.json())
    .then(respuesta => console.log(respuesta));
  }


  */

}
