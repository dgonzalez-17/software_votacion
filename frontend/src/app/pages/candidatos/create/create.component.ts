import { Component, OnInit } from '@angular/core';
import { Candidato } from '../../../models/candidato.model';
import { CandidatoService } from '../../../services/candidato.service';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';

@Component({
  selector: 'ngx-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss']
})
export class CreateComponent implements OnInit {
   
    nombre: string;
    cedula:  string;
    resolucion: string;


  constructor( private candidatoService: CandidatoService, private router: Router ) { }

  ngOnInit(): void {
  }

  crearCandidato(){
    let candidato: Candidato = {
      nombre: this.nombre,
      cedula: this.cedula,
      resolucion: this.resolucion
  }
  this.candidatoService.crearCandidos(candidato).subscribe(
    data=>{
      Swal.fire(
        'Creado!',
        'El candidato ha sido creado correctamente.',
        'success'
      )
      this.router.navigate(['pages/candidatos/read']);
      console.log(data)
    }
  );
}

    /*
create(nombre:string,cedula:string,resolucion:string){



  fetch("http://localhost:3000/candidato/crear",{method: "POST", body: JSON.stringify(candidato), headers: {'Content-Type': 'application/json'}})
  .then(response => response.json())
  .then(respuesta => console.log(respuesta));

}
}
**/
}