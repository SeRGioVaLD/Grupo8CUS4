from utils.db import db
    
class Persona(db.Model):
    __tablename__ = 'persona'
    id_persona = db.Column(db.Integer(), primary_key = True)
    apellido_paterno = db.Column(db.String(60))
    apellido_materno = db.Column(db.String(60))
    nombres = db.Column(db.String(60))
    fecha_nacimiento = db.Column(db.Date())
    id_tipo_documento = db.Column(db.Integer())
    ndocumento = db.Column(db.String(15))
    direccion = db.Column(db.String(150))
    idubigeo = db.Column(db.String(6))