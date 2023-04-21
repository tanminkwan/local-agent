from app import db

class TJob(db.Model):
   id = db.Column(db.Integer, primary_key = True, nullable=False)
   job_code = db.Column(db.String(100), nullable=False)
   job_name = db.Column(db.String(200))

class TPurchase(db.Model):
   id = db.Column(db.Integer, primary_key = True, nullable=False)
   product_code   = db.Column(db.String(100), nullable=False)
   payment_amount = db.Column(db.Integer, nullable=False)
   card_no = db.Column(db.String(100))
   approved_no = db.Column(db.String(100), nullable=False)
   approved_date = db.Column(db.DateTime(), nullable=False)
   refund_no = db.Column(db.String(100))
   refund_date = db.Column(db.DateTime())
   day_refund_yn = db.Column(db.Boolean)