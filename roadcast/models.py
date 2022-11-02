from app import db


class Students(db.Model):
    __tablename__ = "students"
    __bind_key__ = 'db2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    age = db.Column(db.String(255))
    course = db.Column(db.String(255))
    phone_number = db.Column(db.String(10))


class Employee(db.Model):
    __tablename__ = "employee"
    __bind_key__ = 'db1'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    age = db.Column(db.String(255))