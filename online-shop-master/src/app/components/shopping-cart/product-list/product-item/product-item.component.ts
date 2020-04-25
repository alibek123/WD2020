import { Component, OnInit, Input } from '@angular/core';
import {Product} from '../../../../models/product';
import {MessengerService} from '../../../../services/messenger.service';
import {Prod} from '../../../../product';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {

  @Input() productItem: Prod;

  constructor(private msg: MessengerService) { }

  ngOnInit(): void {

  }

  handleAddToCart() {
    this.msg.sendMsg(this.productItem);
  }

}
