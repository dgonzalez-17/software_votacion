import { Component, OnInit, AfterViewInit } from '@angular/core';
import { Candidato } from '../../../models/candidato.model';
import { CandidatoService } from '../../../services/candidato.service';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';
import { ActivatedRoute, Params } from '@angular/router';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';


@Component({
  selector: 'ngx-update',
  templateUrl: './update.component.html',
  styleUrls: ['./update.component.scss']
})
export class UpdateComponent implements OnInit {
  updateForm: FormGroup;
  alertaActiva = false;
  public candidatito: Candidato = this.router.getCurrentNavigation().extras.state.candidato


  constructor (private candidatoService: CandidatoService, private router: Router) { 
    }

  ngOnInit(): void {
    this.initForm();
  
  }
initForm() {
  this.updateForm = new FormGroup({
    _id: new FormControl(this.candidatito._id),
    nombre: new FormControl(this.candidatito.nombre,Validators.compose([Validators.required, Validators.minLength(5)])),
    cedula: new FormControl(this.candidatito.cedula,Validators.compose([Validators.required, Validators.minLength(2)])),
    resolucion: new FormControl(this.candidatito.resolucion,Validators.compose([Validators.required, Validators.minLength(5)])),

  });
}

editarCandidato(){
  let candidato : Candidato = this.updateForm.value
this.candidatoService.editarCandidato(this.candidatito._id, candidato).subscribe(data => {
  Swal.fire(
    'Actualizado!',
    'El candidato ha sido actualizado correctamente.',
    'success'
  ),
  this.router.navigate(['pages/candidatos/read']);
},
error=>{
  Swal.fire({
    title: 'Error, no se pudo actualizar el candiato',
    text: error["error"]["message"],
    icon:"error",
    timer:3000
  });
  this.alertaActiva = true;
}
);

}
}