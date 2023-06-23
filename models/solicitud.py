from utils.db import db

class Solicitud(db.Model):
    __tablename__ = 'solicitud'
    id_solicitud = db.Column(db.Integer(), primary_key = True)
    id_predio = db.Column(db.Integer())
    id_solicitante =  db.Column(db.Integer())
    id_servicio = db.Column(db.Integer())
    area_predio = db.Column(db.Float())
    num_casas = db.Column(db.Integer())
    cant_acomunes = db.Column(db.Integer())
    area_acomunes = db.Column(db.Integer())
    cant_vigilantes = db.Column(db.Integer())
    cant_plimpieza = db.Column(db.Integer())
    cant_administracion = db.Column(db.Integer())
    cant_jardineria = db.Column(db.Integer())
    fecha_solicitud = db.Column(db.Date())
    nombre_solicitante = db.Column(db.String(70))