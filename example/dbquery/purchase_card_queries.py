from example.model.tmodels import TPurchase
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import insert, update
from miniagent import db

def insert_purchase(data: dict):
    
    stmt = insert(TPurchase).values(data)
    db.session.execute(stmt)
    db.session.commit()

def update_purchase(data: dict, condition: dict):

    condition_list = []
    for item in condition:
        col = getattr(TPurchase, item)
        condition_list.append(col==condition[item])
    
    stmt = update(TPurchase).where(*condition_list).values(data)
    r = db.session.execute(stmt)
    print(r)
    db.session.commit()