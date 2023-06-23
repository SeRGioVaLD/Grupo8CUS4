from Google.Google import Create_Service
from Google.ObtenerTokens import obtener_token

def crear_carpeta(nombre):
    CLIENT_SECRET_FILE = "Google/client_secret.json"
    API_NAME = "drive"
    API_VERSION = "v3"
    SCOPES = ["https://www.googleapis.com/auth/drive"]

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    nombreOrigen = "contratos"
    tipo = "application/vnd.google-apps.folder"
    
    token = obtener_token(nombreOrigen,tipo)
    
    folder_id = token
    carpetas = [nombre]

    for carpeta in carpetas:
        file_metadata = {
            "name" : carpeta,
            "parents" : [folder_id],
            "mimeType" : "application/vnd.google-apps.folder"
        }

        service.files().create(body=file_metadata).execute()
        
    nombreOrigen = nombre
    tipo = ["application/vnd.google-apps.folder",None]
    
    token = obtener_token(nombreOrigen,tipo)
    
    folder_id = token
    carpetas = [("datos_solicitante_"+nombre),("datos_personal_"+nombre)]

    for carpeta in carpetas:
        file_metadata = {
            "name" : carpeta,
            "parents" : [folder_id],
            "mimeType" : "application/vnd.google-apps.folder"
        }

        service.files().create(body=file_metadata).execute()
        
        
        
        