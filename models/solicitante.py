from utils.db import db

class Solicitante(db.Model):
    __tablename__ = 'solicitante'
    id_solicitante = db.Column(db.Integer(), primary_key = True)
    id_persona = db.Column(db.Integer())
    id_rol = db.Column(db.Integer())
    telefono = db.Column(db.Integer())
    correo = db.Column(db.String(80))