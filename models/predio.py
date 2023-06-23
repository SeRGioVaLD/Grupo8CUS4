from utils.db import db

class Predio(db.Model):
    __tablename__ = 'predio' 
    id_predio = db.Column(db.Integer(), primary_key = True)
    id_tipo_predio = db.Column(db.Integer())
    descripcion = db.Column(db.String(80))
    ruc = db.Column(db.String(20))
    telefono = db.Column(db.String(12))
    correo = db.Column(db.String(80))
    direccion = db.Column(db.String(100))
    idubigeo = db.Column(db.String(6))
    id_persona = db.Column(db.Integer())