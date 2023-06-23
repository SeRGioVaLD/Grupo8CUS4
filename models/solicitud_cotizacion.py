from utils.db import db

class Solicitud_Cotizacion(db.Model):
    __tablename__ = 'solicitud_cotizacion'
    id_solicitud = db.Column(db.Integer())
    id_personal = db.Column(db.Integer())
    fecha_cotizacion = db.Column(db.Date())
    importe = db.Column(db.Float(6,2))
    id_solicitud_cotizacion = db.Column(db.Integer(), primary_key = True)
    id_estado = db.Column(db.Integer())
    
    
    