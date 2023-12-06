from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(String, primary_key=True, index=True)
    product_name = Column(String, index=True)
    quantity = Column(Integer)
    total_price = Column(Float)
    customer_name = Column(String)
    address = Column(String)
    state = Column(String)
