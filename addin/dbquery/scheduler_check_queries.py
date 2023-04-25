from addin.model.tmodels import THealth
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import insert
from app import db

#def insert_purchase(db: SQLAlchemy,  data: dict):
def add_all_device_health(data: list):
    
    objects = []
    for item in data:
        objects.append(
            THealth(
                adapter_name = item['adapter_name'],
                adaptee_name = item['adaptee_name'],
                is_healthy   = item['is_healthy'],
                checked_date = item['checked_date']
            )
        )
        
    db.session.add_all(objects)
    db.session.commit()