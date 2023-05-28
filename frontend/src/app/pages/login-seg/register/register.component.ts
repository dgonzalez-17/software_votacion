import { Component, OnInit } from '@angular/core';
import { SeguridadService } from '../../../services/seguridad.service';
import { Usuario } from '../../../models/usuario.model';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';

@Component({
  selector: 'ngx-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  nombre: string;
  correo: string;
  contrasena: string;

  constructor(private seguridadService: SeguridadService, private router: Router) { }

  ngOnInit(): void {
    
  }

crearUsuario(): void {
  let usuario: Usuario = {
    nombre: this.nombre,
    correo: this.correo,
    contrasena: this.contrasena,
  }
  this.seguridadService.crearUsuario(usuario).subscribe(
    data=>{
      Swal.fire(
        'Creado!',
        'El candidato ha sido creado correctamente.',
        'success'
      ),
      this.router.navigate(['auth/Listar usuarios']);
      console.log(data)
    });
}

}
