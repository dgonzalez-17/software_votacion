import { Component, OnInit } from '@angular/core';
import { Usuario } from '../../../models/usuario.model';
import { SeguridadService } from '../../../services/seguridad.service';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';

@Component({
  selector: 'ngx-read',
  templateUrl: './read.component.html',
  styleUrls: ['./read.component.scss']
})
export class ReadComponent implements OnInit {

  usuarios: Usuario[] = [];

  constructor(private seguridadService: SeguridadService, private router: Router) { }

  consultarUsuario(): void {
    this.seguridadService.consultarUsuarios().subscribe(usuarios => {
      this.usuarios = usuarios;
    });
  }

  crearUsuario(): void {
    this.router.navigate(['auth/register']);

  }

  editarUsuario(id:string, usuario: Usuario): void {
    this.router.navigate(['pages/login-seg/update/'+id], {state:{ id: id, usuario: usuario}} );
  }

  eliminarUsuario(id:string){
    Swal.fire({
      title: 'Está a punto de eliminar un usuario.',
      text: "¿Está seguro de que desea eliminar este usuario?",
      icon:"warning",
      showCancelButton: true,
      confirmButtonColor: "green",
      cancelButtonColor: "orange",
      confirmButtonText: 'Si, eliminar'
    }).then((result) => {
      if (result.isConfirmed){
    this.seguridadService.eliminarUsuario(id).subscribe(
      data => {
        Swal.fire(
          'Elminado!',
          'El usuario ha sido eliminado correctamente.',
          'success'
        )
        this.ngOnInit();
      });
  }
})
}

  

  ngOnInit(): void {
    this.consultarUsuario();
  }

}
