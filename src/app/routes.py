from fastapi import FastAPI, Request, HTTPException, Depends, status
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from . import crud, models  
from .database import SessionLocal, engine
from .schemas import OrderCreate, Order  

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/', status_code=status.HTTP_201_CREATED, response_model=Order)
async def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_order(db=db, order=order)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/', response_class=HTMLResponse)
async def get_products(request: Request, db: Session = Depends(get_db)):
    products = crud.get_products(db)
    return templates.TemplateResponse("index.html", {"request": request, "products": products, "states": state_abbreviations})

@app.get('/orders/{order_id}', response_model=Order)
async def get_order(order_id: str, db: Session = Depends(get_db)):
    db_order = crud.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@app.get('/orders/{order_id}', response_class=HTMLResponse)
async def view_order(request: Request, order_id: str, db: Session = Depends(get_db)):
    db_order = crud.get_order(db, order_id=order_id)
    if db_order is None:
        content = {"request": request, "order_id": order_id, "error": "Order not found"}
    else:
        popular_products = crud.find_popular_products(state=db_order.state, db=db)
        content = {"request": request, "order": db_order, "popular_products": popular_products}
    return templates.TemplateResponse("view_order.html", content)

@app.get('/get_product/')
async def get_product(product_name: str, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_name=product_name)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.get('/health_check')
async def health_check():
    return {'message': 'Healthy :)'}