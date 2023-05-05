import {Injectable} from '@angular/core';
import {Observable} from "rxjs";
import {AuthToken, Product} from "./models";
import {HttpClient} from "@angular/common/http";
@Injectable({
  providedIn: 'root'
})
export class ProductService {

  BASE_URL = 'http://localhost:8000'

  constructor(private client: HttpClient) {
  }

  getProducts(): Observable<Product[]> {
    return this.client.get<Product[]>(
      `${this.BASE_URL}/api/Products/`
    )
  }

  createProduct(ProductName: string): Observable<Product> {
    return this.client.post<Product>(
      `${this.BASE_URL}/api/Products/`,
      {name: ProductName}
    )
  }

  deleteProduct(Product_id: number): Observable<any> {
    return this.client.delete(
      `${this.BASE_URL}/api/products/${Product_id}/`
    )
  }
}
