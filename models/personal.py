from utils.db import db
    
class Personal(db.Model):
    __tablename__ = 'personal'
    id_personal = db.Column(db.Integer(), primary_key = True)
    id_persona = db.Column(db.Integer())
    id_rol = db.Column(db.Integer())
    fecha_contrato = db.Column(db.Date())
    fecha_cese = db.Column(db.Date())