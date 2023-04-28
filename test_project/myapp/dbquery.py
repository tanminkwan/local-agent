
from myapp.model.mymodels import THealth
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import insert
from miniagent import db

def add_all_adapters_health(data: list):
    
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