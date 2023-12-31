from googleapiclient.http import MediaFileUpload
from Google.Google import Create_Service, getCarpetID

def subir_archivo(carpeta):
    CLIENT_SECRET_FILE = "client_secret.json"
    
    API_NAME = "drive"
    API_VERSION = "v3"
    SCOPES = ["https://www.googleapis.com/auth/drive"]

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    folder_id = getCarpetID( CLIENT_SECRET_FILE,  SCOPES, carpeta)
    file_names = ["nombre del archivo"]
    mime_types = ["image/*   <-- en el caso de que se una imagen"]

    for file_name, mime_type in zip(file_names, mime_types):
        file_metadata = {
            "name" : file_name,
            "parents" : [folder_id]
        }

        media = MediaFileUpload("./Drive/{0}".format(file_name), mimetype=mime_type)

        service.files().create(
            body=file_metadata,
            media_body = media,
            fields = "id"
        ).execute()