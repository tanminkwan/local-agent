import enum
from . import db

class YesNoEnum(enum.Enum):
   YES = "YES"
   NO  = "NO"
   
class Job(db.Model):
   id = db.Column(db.Integer, primary_key = True, nullable=False)
   job_code = db.Column(db.String(100), nullable=False)
   job_name = db.Column(db.String(200))