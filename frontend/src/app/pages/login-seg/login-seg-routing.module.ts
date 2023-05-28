import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { ReadComponent } from './read/read.component';
import { UpdateComponent } from './update/update.component';

const routes: Routes = [
{
  path: 'login',
  component: LoginComponent
},
{
  path: 'Register',
  component: RegisterComponent
},

{
  path: 'Listar Usuarios',
  component: ReadComponent
},
{
  path: 'update/:id',
  component: UpdateComponent
},
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class LoginSegRoutingModule { }
