from flaskinventory import db
from datetime import datetime

class Location(db.Model):
    loc_id = db.Column(db.Integer, primary_key= True)
    loc_name = db.Column(db.String(20),unique = True, nullable = False)

    def __repr__(self):
        return f"Location('{self.loc_id}','{self.loc_name}')"
        return "Location('{self.loc_id}','{self.loc_name}')"

class Product(db.Model):
    prod_id = db.Column(db.Integer, primary_key= True)
    prod_name = db.Column(db.String(20), nullable = False)
    prod_name = db.Column(db.String(20),unique = True ,nullable = False)
    prod_qty = db.Column(db.Integer, nullable = False)
    def __repr__(self):
        return f"Product('{self.prod_id}','{self.prod_name}','{self.prod_qty}')"

class Movement(db.Model):
    mid = db.Column(db.Integer, primary_key= True)
    ts = db.Column(db.DateTime, default=datetime.utcnow)
    frm = db.Column(db.String(20), nullable = False)
    to = db.Column(db.String(20), nullable = False)
    pname = db.Column(db.String(20), nullable = False)
    pqty = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Movement('{self.mid}','{self.ts}','{self.frm}','{self.to}','{self.pname}','{self.pqty}')"

class Balance(db.Model):
    bid = db.Column(db.Integer, primary_key= True,nullable = False)
    product = db.Column(db.String(20), nullable = False)
    location = db.Column(db.String(20),nullable = False)
    quantity = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Balance('{self.bid}','{self.product}','{self.location}','{self.quantity}')"
