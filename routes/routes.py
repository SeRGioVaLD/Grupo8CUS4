from flask import Blueprint,render_template, request, redirect, url_for, flash, session

from models.tipo_predio import Tipo_Predio
from models.ubigeo import Ubigeo
from models.predio import Predio
from models.area_comun import Area_Comun
from models.predio_area_comun import Predio_Area_Comun
from models.servicio import Servicio
from models.solicitud_cotizacion import Solicitud_Cotizacion
from models.solicitud import Solicitud
from models.rol import Rol
from models.tipo_documento import Tipo_Documento
from models.persona import Persona
from models.personal import Personal
from models.solicitante import Solicitante
from models.contrato import Contrato
from datetime import datetime

from Google.Carpetas import crear_carpeta
from Google.CargarDatosContrato import obtener_links


from utils.db import db

routes = Blueprint("routes", __name__)

routes.secret_key = 'clave_secreta'

@routes.route('/')
def index():
    
    
    
    return render_template('index.html')   
        
@routes.route('/usuario', methods=['POST'])
def usuario():
    if request.method == 'POST':
        id = request.form['id']
        return redirect(url_for('routes.personal', id=id))
    
@routes.route('/personal/<id>')
def personal(id):
    return render_template(
        'personal_templates/pagina_personal.html',
        id=id
    )   

@routes.route('/contratos/<id>', methods=['POST','GET'])
def contratos(id):
    id_personal = int(id)
    
    
    cotizaciones = Solicitud_Cotizacion.query.filter(
        Solicitud_Cotizacion.id_personal == id_personal,
        ~Solicitud_Cotizacion.id_solicitud_cotizacion.in_(
            db.session.query(Contrato.id_solicitud_cotizacion)
        ),
        (Solicitud_Cotizacion.id_estado == 1) | 
        (Solicitud_Cotizacion.id_estado == None)
    ).all()
    
    
    contratos_pendientes = Contrato.query.filter(
        Contrato.id_personal == id_personal,
        Contrato.fecha_contrato != None,
        Contrato.fecha_firma_solicitante != None,
        Contrato.fecha_firma_personal == None,
    ).all()
    
    
    contratos_registrados = Contrato.query.filter(
        Contrato.id_personal == id_personal,
        Contrato.fecha_contrato != None,
        Contrato.fecha_firma_solicitante != None,
        Contrato.fecha_firma_personal != None,
        Contrato.fecha_registro != None,
    ).all()
    
    print("CONTRATOS_REGISTRADOS: ",contratos_registrados)
    
    return render_template(
        'personal_templates/contratos_personal.html',
        id=id,
        cotizaciones=cotizaciones,
        contratos_pendientes = contratos_pendientes,
        contratos_registrados = contratos_registrados
    )
        
        
@routes.route('/crear_contrato/<id>/<id_solicitud_cotizacion>', methods=['POST'])
def crear_contrato(id,id_solicitud_cotizacion):
    
    print("id->",id)
    print("id_solicitud_cotizacion->",id_solicitud_cotizacion)

    
    cotizacion = Solicitud_Cotizacion.query.filter(
        Solicitud_Cotizacion.id_solicitud_cotizacion == id_solicitud_cotizacion
    ).all()
    
    
    solicitud = Solicitud.query.filter(
        Solicitud.id_solicitud == cotizacion[0].id_solicitud    
    ).all()
    
    id_personal = id
    id_solicitante = solicitud[0].id_solicitante
    
    nombre_carpeta = "contrato-"+str(id_solicitud_cotizacion)+"-"+str(id_personal)+"-"+str(id_solicitante)    
    crear_carpeta(nombre_carpeta)
    
    
    contrato = Contrato(id_solicitud_cotizacion,
                        id_personal,
                        id_solicitante,
                        datetime.now().date(), 
                        None,
                        None,
                        None,
                        None)
    db.session.add(contrato)
    db.session.commit()
    
    
    return redirect(url_for('routes.contratos', id=id))


@routes.route('/firmar_contrato/<id>/<id_contrato>', methods=['POST'])
def firmar_contrato(id,id_contrato):
    
    print("id->",id)
    print("id_contrato->",id_contrato)

    contrato = Contrato.query.get(id_contrato)
    
    print(id)
    print(contrato.id_personal)
    
    personal = Personal.query.get(contrato.id_personal)
    
    
    solicitante = Solicitante.query.get(contrato.id_solicitante)
    
    cotizacion = Solicitud_Cotizacion.query.get(contrato.id_solicitud_cotizacion)
    
    solicitud = Solicitud.query.get(cotizacion.id_solicitud)
    servicio = Servicio.query.get(solicitud.id_servicio)
    
    predio = Predio.query.get(solicitud.id_predio)
    ubigeo_predio = Ubigeo.query.get(predio.idubigeo)
    tipo_predio = Tipo_Predio.query.get(predio.id_tipo_predio)
    
    consulta_area_comun = db.session.query(Predio_Area_Comun, Area_Comun).join(Area_Comun, Predio_Area_Comun.id_area_comun == Area_Comun.id_area_comun)
    consulta_area_comun = consulta_area_comun.filter(Predio_Area_Comun.id_predio == predio.id_predio).all()

    predio_area_comun = []
    area_comun = []
    if len(consulta_area_comun) > 0:
        consulta = consulta_area_comun[0]
        predio_area_comun.append(consulta[0])
        area_comun.append(consulta[1])
        
    print(predio_area_comun)
    print(area_comun)
    
    persona_personal = Persona.query.get(personal.id_persona)
    rol_personal = Rol.query.get(personal.id_rol)
    tipo_documento_personal = Tipo_Documento.query.get(persona_personal.id_tipo_documento)
    
    persona_solicitante = Persona.query.get(solicitante.id_persona)
    rol_solicitante = Rol.query.get(solicitante.id_rol)
    tipo_documento_solicitante = Tipo_Documento.query.get(persona_solicitante.id_tipo_documento)
    
    nombre_carpeta = "contrato-"+str(cotizacion.id_solicitud_cotizacion)+"-"+str(personal.id_personal)+"-"+str(solicitante.id_solicitante)    
    
    firma_solicitante_link,huella_solicitante_link,firma_personal_link,huella_personal_link = obtener_links(nombre_carpeta)
    
    return render_template(
        'contrato_templates/contrato.html',
        id=id,
        contrato = contrato,
        personal = personal,
        solicitante = solicitante,
        cotizacion = cotizacion,
        solicitud = solicitud,
        servicio = servicio,
        predio = predio,
        ubigeo_predio = ubigeo_predio,
        tipo_predio = tipo_predio,
        predio_area_comun = predio_area_comun,
        area_comun = area_comun,
        
        persona_personal = persona_personal,
        rol_personal = rol_personal,
        tipo_documento_personal = tipo_documento_personal,
        
        persona_solicitante = persona_solicitante,
        rol_solicitante = rol_solicitante,
        tipo_documento_solicitante = tipo_documento_solicitante,
        
        firma_solicitante_link = firma_solicitante_link,
        huella_solicitante_link = huella_solicitante_link,
        firma_personal_link = firma_personal_link,
        huella_personal_link = huella_personal_link
    )