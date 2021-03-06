import {Component, OnInit} from '@angular/core';
import {ProductService} from '../product.service';
import {Category} from '../category';
import {PRODUCTS} from '../products';

@Component({
  selector: 'app-categories',
  templateUrl: './categories.component.html',
  styleUrls: ['./categories.component.css']
})
export class CategoriesComponent implements OnInit {
  categories: Category[];
  product = PRODUCTS;

  constructor(private productService: ProductService) {
  }

  ngOnInit(): void {
    this.getCategories();
  }

  getCategories() {

    this.productService.getCategory()
      .subscribe(categories => this.categories = categories);
  }

}
