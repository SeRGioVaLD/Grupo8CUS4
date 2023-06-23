from utils.db import db

class Tipo_Documento(db.Model):
    __tablename__ = 'tipo_documento'
    id_tipo_documento = db.Column(db.Integer(), primary_key = True)
    descripcion = db.Column(db.String(20))