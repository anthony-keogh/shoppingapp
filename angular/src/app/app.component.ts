import { Component } from '@angular/core';
import { ProductService } from './product.service';
import { Product } from './product';
import { Input, Output, EventEmitter } from '@angular/core';


@Component({
  selector: 'app-root',
  
  templateUrl: './app.component.html',
  
})


export class AppComponent
{
   title = 'angular';

   products:Product[];
   productService;
 
   constructor(){
     this.productService=new ProductService();
   }
 
   getProducts() {
     
     this.products=this.productService.getProducts();
   }

   @Input() count: number = 0;
    @Output() countChange: EventEmitter<number> = new EventEmitter<number>();
   
    increment() {
     this.count++;
     this.countChange.emit(this.count);
   }
  
}

