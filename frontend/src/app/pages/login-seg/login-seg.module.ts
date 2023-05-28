import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NbMenuModule, NbCardModule, NbInputModule, NbButtonModule } from '@nebular/theme';
import { LoginSegRoutingModule } from './login-seg-routing.module';
import { SweetAlert2Module } from '@sweetalert2/ngx-sweetalert2';
import { LoginComponent } from './login/login.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RegisterComponent } from './register/register.component';
import { ReadComponent } from './read/read.component';
import { UpdateComponent } from './update/update.component';


@NgModule({
  declarations: [
    LoginComponent,
    RegisterComponent,
    ReadComponent,
    UpdateComponent
  ],
  imports: [
    CommonModule,
    LoginSegRoutingModule,
    NbCardModule,
    NbInputModule,
    NbButtonModule,
    FormsModule,
    SweetAlert2Module,
    ReactiveFormsModule
  ]
})
export class LoginSegModule { }
