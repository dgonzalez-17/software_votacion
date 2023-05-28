import { Component, OnInit } from '@angular/core';
import { Candidato } from '../../../models/candidato.model';
import { CandidatoService } from '../../../services/candidato.service';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';

@Component({
  selector: 'ngx-read',
  templateUrl: './read.component.html',
  styleUrls: ['./read.component.scss']
})
export class ReadComponent implements OnInit {

  candidatos: Candidato[] = []

  constructor(private candidatoService: CandidatoService, private router: Router) { }

  crearCandidato():void{
    this.router.navigate(['pages/candidatos/create']);
  }

  consultarCandidatos():void{
    this.candidatoService.consultarCandidatos().subscribe(candidatoConsulta => {
      this.candidatos = candidatoConsulta
    });
  }
  editarCandidato(id: string, candidato: Candidato):void{
    this.router.navigate(['pages/candidatos/update/'+id], {state:{id: id, candidato: candidato}});
  }

  eliminarCandidato(id:string):void{
    Swal.fire({
      title: 'Está a punto de eliminar un candidato.',
      text: "¿Está seguro de que desea eliminar este candidato?",
      icon:"warning",
      showCancelButton: true,
      confirmButtonColor: "green",
      cancelButtonColor: "orange",
      confirmButtonText: 'Si, eliminar'
    }).then((result) => {
      if (result.isConfirmed){
    this.candidatoService.eliminarCandidato(id).subscribe(
      data => {
        Swal.fire(
          'Elminado!',
          'El candidato ha sido eliminado correctamente',
          'success'
        )
        this.ngOnInit();
      });
  }
})
}

  ngOnInit(): void {
    this.consultarCandidatos()
  }

}
