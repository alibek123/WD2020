import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {LoginComponent} from './components/shared/login/login.component';
import {RegisterComponent} from './components/register/register.component';
import {CategoryListComponent} from './components/shopping-cart/product-list/category-list/category-list.component';
// import {ProductListComponent} from './components/shopping-cart/product-list/product-list.component';
import {ProductItemComponent} from './components/shopping-cart/product-list/product-item/product-item.component';
import {AccessoriesComponent} from './components/shopping-cart/product-list/accessories/accessories.component';


const routes: Routes = [
  {path: '', redirectTo: '/categories/1', pathMatch: 'full'},
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  // { path: 'categories/:id', component: ProductListComponent},
  { path: 'products/:id', component: ProductItemComponent},
  { path: 'categories/:id', component: CategoryListComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
