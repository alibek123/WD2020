export class Product {
  id: number;
  name: string;
  description: string;
  price: number;

  // tslint:disable-next-line:max-line-length
  // imgUrl = 'https://img.pngio.com/product-icon-png-76431-free-icons-library-product-png-256_256.jpg'
  constructor(id, name, description = '', price = 0) {
    this.id = id;
    this.name = name;
    this.description = description;
    this.price = price;
  }
}
