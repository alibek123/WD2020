import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CategoriesComponent } from './categories/categories.component';
import { ProductsComponent } from './products/products.component';
import { TopBarComponent } from './top-bar/top-bar.component';
import { ProductdetailsComponent } from './productdetails/productdetails.component';

@NgModule({
  declarations: [
    AppComponent,
    TopBarComponent,
    CategoriesComponent,
    ProductsComponent,
    ProductdetailsComponent
  ],
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
