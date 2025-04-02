from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os

# Definir los permisos de acceso
SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate_drive():
    creds = None
    # Cargar credenciales desde archivo
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # Si no hay credenciales válidas, pedir autenticación
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '/Users/tadeonava/Python/API_drive.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Guardar credenciales en un archivo pickle
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

# Autenticarse
creds = authenticate_drive()
print("✅ Autenticación exitosa")


