from typing import List, Optional
from pydantic import BaseModel, Field, UUID4

class Product(BaseModel):
    product_name: str
    price: float
    description: str
    image: str
    num_in_stock: int

class OrderBase(BaseModel):
    product_name: str
    quantity: int
    total_price: float
    customer_name: str
    address: str
    state: str

# Schema for request when creating an order
class OrderCreate(OrderBase):
    pass

# Schema for response when retrieving an order
class Order(OrderBase):
    order_id: UUID4

class ProductList(BaseModel):
    products: List[Product]

class PopularProduct(BaseModel):
    product_name: str
    num_orders: int

class PopularProducts(BaseModel):
    popular_products: List[PopularProduct]
