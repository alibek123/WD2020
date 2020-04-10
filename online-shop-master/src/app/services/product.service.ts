import {Injectable} from '@angular/core';

// import {Product} from '../models/product';
import {Observable, of} from 'rxjs';
import {CATEGORIES} from '../models/categories';
import {Category} from '../models/category';
import {PRODUCTS} from '../products';
import {Prod} from '../product';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  //  products: Product[] = [
  //   new Product(1, 'Product 1', 'This is the product 1 description. The product is really cool!', 100),
  //   new Product(2, 'Product 2', 'This is the product 2 description. The product is really cool!', 250),
  //   new Product(3, 'Product 3', 'This is the product 3 description. The product is really cool!', 150),
  //   new Product(4, 'Product 4', 'This is the product 4 description. The product is really cool!', 1450),
  //   new Product(5, 'Product 5', 'This is the product 5 description. The product is really cool!', 8480),
  //   new Product(6, 'Product 6', 'This is the product 6 description. The product is really cool!', 840),
  //   new Product(7, 'Product 7', 'This is the product 7 description. The product is really cool!', 1480),
  //   new Product(8, 'Product 8', 'This is the product 8 description. The product is really cool!', 1770),
  //   new Product(9, 'Product 9', 'This is the product 9 description. The product is really cool!', 10480),
  //   new Product(10, 'Product 10', 'This is the product 10 description. The product is really cool!', 14840)
  // ];


  // getProducts(): Product[] {
  //   return this.products;
  // }

  getHeroes(): Prod[] {
    return PRODUCTS;
  }

  getCategory(): Observable<Category[]> {
    return of(CATEGORIES);
  }

  getCategories(id: number): Observable<Category> {
    return of(CATEGORIES.find(category => category.id === id));


  }
}
