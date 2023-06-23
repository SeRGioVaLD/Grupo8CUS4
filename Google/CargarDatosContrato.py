from Google.Google import Create_Service
from Google.ObtenerTokens import obtener_token

def obtener_links(nombre_contrato):
    CLIENT_SECRET_FILE = "Google/client_secret.json"
    API_NAME = "drive"
    API_VERSION = "v3"
    SCOPES = ["https://www.googleapis.com/auth/drive"]

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    tipo = ["image/png","image/jpeg"]
    
    firma_solicitante = "firma_solicitante_"+nombre_contrato+".jpg"
    huella_solicitante = "huella_solicitante_"+nombre_contrato+".jpg"
    firma_personal = "firma_personal_"+nombre_contrato+".jpg"
    huella_personal = "huella_personal_"+nombre_contrato+".jpg"
    vacio = "Vacio.png"
    
    firma_solicitante_token = obtener_token(firma_solicitante,tipo)
    huella_solicitante_token = obtener_token(huella_solicitante,tipo)
    firma_personal_token = obtener_token(firma_personal,tipo)
    huella_personal_token = obtener_token(huella_personal,tipo)
    vacio_token = obtener_token(vacio,tipo)
    
    print("VACIO TOKENNN OBTENIDO: ",vacio_token)
    print("firma_solicitante_token TOKENNN OBTENIDO: ",firma_solicitante_token )
    print("huella_solicitante_token OBTENIDO: ",huella_solicitante_token)
    print("firma_personal_token: ",firma_personal_token)
    print("huella_personal_token : ",huella_personal_token )
    
    print("VACIO TOKENNN REAL 13rN0cFGUvPfjK0YieXN97vaapuIsGQux")
    
    if firma_solicitante_token :
        firma_solicitante_link = "https://drive.google.com/uc?export=view&id="+str(firma_solicitante_token)
    else:
        firma_solicitante_link = "https://drive.google.com/uc?export=view&id="+str(vacio_token)
    
    if huella_solicitante_token :
        huella_solicitante_link = "https://drive.google.com/uc?export=view&id="+str(huella_solicitante_token)
    else:
        huella_solicitante_link = "https://drive.google.com/uc?export=view&id="+str(vacio_token)
        
        
    
    if firma_personal_token:
        firma_personal_link = "https://drive.google.com/uc?export=view&id="+str(firma_personal_token)
    else:
        firma_personal_link = "https://drive.google.com/uc?export=view&id="+str(vacio_token)
    
    if huella_personal_token :
        huella_personal_link = "https://drive.google.com/uc?export=view&id="+str(huella_personal_token)
    else:
        huella_personal_link = "https://drive.google.com/uc?export=view&id="+str(vacio_token)
    
    
    print("LINK-firma_solicitante_token TOKENNN OBTENIDO: ",firma_solicitante_link)
    print("LINK-huella_solicitante_token OBTENIDO: ",huella_solicitante_link)
    print("LINK-firma_personal_token: ",firma_personal_link)
    print("LINK-huella_personal_token : ",huella_personal_link)
    
    
    return firma_solicitante_link,huella_solicitante_link,firma_personal_link,huella_personal_link