from utils.db import db

class Rol(db.Model):
    __tablename__ = 'rol'
    id_rol = db.Column(db.Integer(), primary_key = True)
    descripcion = db.Column(db.String(60))