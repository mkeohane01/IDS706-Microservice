from sqlalchemy.orm import Session
from . import models, schemas
import uuid

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(
        order_id=str(uuid.uuid4()),
        product_name=order.product_name,
        quantity=order.quantity,
        total_price=order.total_price,
        customer_name=order.customer_name,
        address=order.address,
        state=order.state
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, order_id: str):
    return db.query(models.Order).filter(models.Order.order_id == order_id).first()