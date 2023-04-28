# Write code using miniagent.db
#, which is the instance of SQLALCHEMY
# You can add your own tables' definition like below class THealth 

from miniagent import db
from miniagent.models import YesNoEnum
from sqlalchemy import Enum

class THealth(db.Model):
   id = db.Column(db.Integer, primary_key = True, nullable=False)
   adapter_name = db.Column(db.String(300), nullable=False)
   adaptee_name = db.Column(db.String(300))
   is_healthy = db.Column(Enum(YesNoEnum), nullable=False)
   checked_date = db.Column(db.DateTime(), nullable=False)