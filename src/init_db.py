from app import app, db
from app.datapipe import Order

with app.app_context():
    db.create_all()
