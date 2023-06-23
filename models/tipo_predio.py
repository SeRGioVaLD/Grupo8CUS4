from utils.db import db

class Tipo_Predio(db.Model):
    __tablename__ = 'tipo_predio'
    id_tipo_predio = db.Column(db.Integer(), primary_key = True)
    nomre_predio = db.Column(db.String())     