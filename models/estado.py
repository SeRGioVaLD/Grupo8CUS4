from utils.db import db

class Estado(db.Model):
    __tablename__ = 'estado'
    id_estado = db.Column(db.Integer(), primary_key = True)
    descripcion = db.Column(db.String(15)) 