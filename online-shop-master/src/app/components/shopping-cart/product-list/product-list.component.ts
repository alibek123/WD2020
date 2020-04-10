import {Component, Input, OnInit} from '@angular/core';
import {ProductService} from '../../../services/product.service';
import {Prod} from '../../../product';
import {Product} from '../../../models/product';
import {MessengerService} from '../../../services/messenger.service';
// import {Product} from '../../../models/product';
// import {Observable} from 'rxjs';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {

  productList: any[] = [];
  products: Prod[];
  @Input() productItem: Prod;

  constructor(private productService: ProductService,
              private msg: MessengerService) {
  }

  ngOnInit(): void {
    // this.productList = this.productService.getProducts();
    this.getProd();
  }

  handleAddToCart() {
    this.msg.sendMsg(this.productItem);
  }

  getProd(): void {
    this.products = this.productService.getHeroes();
  }


}
