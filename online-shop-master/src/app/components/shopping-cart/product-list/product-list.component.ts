import {Component, Input, OnInit} from '@angular/core';
import {ProductService} from '../../../services/product.service';
import {Prod} from '../../../product';
import {Product} from '../../../models/product';
import {MessengerService} from '../../../services/messenger.service';
import {Category} from '../../../models/category';
import {ActivatedRoute} from '@angular/router';
import {PRODUCTS} from '../../../products';
// import {Product} from '../../../models/product';
// import {Observable} from 'rxjs';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {

  productList: Prod[] = [];
  listSorted: any[] = [];
  products: Prod[];
  @Input() productItem: Prod;
  categories: Category[];


  constructor(private productService: ProductService,
              private msg: MessengerService,
              private route: ActivatedRoute) {
  }

  ngOnInit(): void {
    // this.productList = this.productService.getProducts();
    this.getProd();
    // const id = +this.route.snapshot.paramMap.get('id');
    // this.sort(id);
  }

  sort(id: number): void {
    for (const p in PRODUCTS) {
      if (this.productList[p].categoryId === id) {
        this.listSorted.push(this.productList[p]);
      }
    }
  }

  handleAddToCart() {
    this.msg.sendMsg(this.productItem);
  }


  // getProds(): void {
  //   this.products = this.productService.getProducts();
  // }
  getProd(): void {
    this.productService.getProducts()
      .subscribe(product => this.products = product);
  }

  // getProd(): void {
  //   const id = +this.route.snapshot.paramMap.get('id');
  //   this.productService.getProductofC(id)
  //     .subscribe(products => this.products = products);
  // }

}
