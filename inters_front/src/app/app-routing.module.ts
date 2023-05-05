import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
// import {HTTP_INTERCEPTORS, HttpClientModule} from "@angular/common/http";
// import {FormsModule} from "@angular/forms";
// import {AuthInterceptor} from "./AuthInterceptor";
import { ProductListComponent } from './product-list/product-list.component';
import { ProductDetailComponent } from './product-detail/product-detail.component';
import { ProfilComponent } from './profil/profil.component';
import { DistrictsComponent } from './districts/districts.component';
import { CartComponent } from './cart/cart.component';
// import { RouterModule } from '@angular/router';
import { DistrictDetailComponent } from './district-detail/district-detail.component';
const routes: Routes = [
  {path:'products', component:ProductListComponent},
    {path:'districts', component: DistrictsComponent},
    {path:'districts/:districtID', component:DistrictDetailComponent},
    { path: 'district/:districtID/products/:productId', component: ProductDetailComponent },
    { path: 'cart', component: CartComponent },
    { path: 'profil', component: ProfilComponent },
    
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
