import {Product} from './Product'
 
export class ProductService{
 
    public  getProducts() {
 
        let products:Product[];
 
        products=[
            new Product(1,'Floral Blue Dress',65),
            new Product(2,'Light Pink Dress',50),
            new Product(3,'White Rose Dress',68),
            new Product(4,'Silk Blue Jeans',55),
            new Product(5,'Dark Blue Jeans',45),
            new Product(6,'Classic Blue Jeans',40),
            new Product(7,'Box Striped Coat',90),
            new Product(8,'Dark Red Coat',70),
            new Product(9,'Baileys Cream Coat',105),
            new Product(10,'Wood Brown Coat',75),
            new Product(11,'Sun Yellow Coat',79),
            new Product(12,'Black Coat',100),

            new Product(13,'Pink Rose Dress',75),
            new Product(14,'Red Dress',75),
            new Product(15,'Pink Silk Dress',75),
            new Product(16,'Black Floral Dress',65),
            new Product(17,'Blue Stripe Coat',75),
            new Product(18,'White Dress',75),

            new Product(13,'Navy Top',45),
            new Product(14,'Yellow Dotted Top',55),
            new Product(15,'Pink top',42),
            new Product(16,'Brown Polo-Neck',65),
            new Product(17,'Mango Jumper',50),
            new Product(18,'White Jumper',45),

            new Product(19,'Faded blue Top',40),
            new Product(20,'Black Top',60),
            new Product(21,'Red Top',45),

            new Product(22,'Cut Jeans ',65),
            new Product(23,'Faded Blue Jeans',54),
            new Product(24,'Light Cut Jeans',60)
        ]
 
        return products;               
    }
}