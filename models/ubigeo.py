from utils.db import db

class Ubigeo(db.Model):
    __tablename__ = 'ubigeo'
    idubigeo = db.Column(db.String(6), primary_key = True)
    departamento = db.Column(db.String(60))
    provincia = db.Column(db.String(60))
    distrito = db.Column(db.String(60))
    superficie = db.Column(db.Float(10,4))
    altitud = db.Column(db.Float(10,4))
    latitud = db.Column(db.Float(10,4))
    longitud = db.Column(db.Float(10,4))