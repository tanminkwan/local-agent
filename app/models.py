from . import db

class Job(db.Model):
   id = db.Column(db.Integer, primary_key = True, nullable=False)
   job_code = db.Column(db.String(100), nullable=False)
   job_name = db.Column(db.String(200))