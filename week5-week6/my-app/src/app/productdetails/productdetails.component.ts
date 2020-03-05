import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import {ProductService} from '../product.service';
import {Product} from '../product';
import {Category} from '../category'
@Component({
  selector: 'app-productdetails',
  templateUrl: './productdetails.component.html',
  styleUrls: ['./productdetails.component.css']
})
export class ProductdetailsComponent implements OnInit {
  categories: Category[];
  product: Product;
  constructor(
    private location: Location,
    private route: ActivatedRoute,
    private productService: ProductService
    ){}

  ngOnInit(): void {
    this.getProduct();
  }

  getProduct(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.productService.getProduct(id)
      .subscribe(item => this.product = item);
  }
 

}
