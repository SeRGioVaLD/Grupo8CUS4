from Google.Google import Create_Service

def crear_carpeta(nombre):
    CLIENT_SECRET_FILE = "Google/client_secret.json"
    API_NAME = "drive"
    API_VERSION = "v3"
    SCOPES = ["https://www.googleapis.com/auth/drive"]

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    carpetas = [nombre]

    for carpeta in carpetas:
        file_metadata = {
            "name" : carpeta,
            "mimeType" : "application/vnd.google-apps.folder"
        }

        service.files().create(body=file_metadata).execute()