import { Component, OnInit } from '@angular/core';
import { Usuario } from '../../../models/usuario.model';
import { SeguridadService } from '../../../services/seguridad.service';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';
import { FormControl, FormGroup, Validators } from '@angular/forms';


@Component({
  selector: 'ngx-update',
  templateUrl: './update.component.html',
  styleUrls: ['./update.component.scss']
})
export class UpdateComponent implements OnInit {
  updateForm: FormGroup;
  alertaActiva = false;
  public usuarioLlegada : Usuario = this.router.getCurrentNavigation().extras.state.usuario;

  constructor(private seguridadService: SeguridadService, private router: Router) { }

  ngOnInit(): void {
    this.initForm();
  }
  initForm() {
    this.updateForm = new FormGroup({
      _id: new FormControl(this.usuarioLlegada._id),
      nombre: new FormControl(this.usuarioLlegada.nombre,Validators.compose([Validators.required, Validators.minLength(5)])),
      correo: new FormControl(this.usuarioLlegada.correo,Validators.compose([Validators.required, Validators.minLength(2)])),
      contrasena: new FormControl(this.usuarioLlegada.contrasena,Validators.compose([Validators.required, Validators.minLength(5)])),
  
    });
  }

  editarUsuario(){
    let usuario : Usuario = this.updateForm.value;
    this.seguridadService.editarUsuario(this.usuarioLlegada._id, usuario).subscribe (data=>{
      Swal.fire(
        'Actualizado!',
        'El usuario ha sido actualizado correctamente.',
        'success'
      ),
      this.router.navigate(['auth/login']);
    },
    error=>{
      Swal.fire({
        title: 'Error, no se pudo actualizar el usuario.',
        text: error["error"]["message"],
        icon:"error",
        timer:3000
      });
      this.alertaActiva = true;

    });

  }


}
