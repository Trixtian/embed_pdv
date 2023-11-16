
from flask import current_app as app  # Importa el módulo 'current_app' de Flask.
import msal  # Importa la Biblioteca de Autenticación de Microsoft (msal).

class AadService:
    def get_access_token():
        '''Genera y devuelve un token de acceso
        
        Devuelve:
            str: Token de acceso
        '''

        response = None  # Inicializa la variable 'response' como nula.
        try:
            # Verifica el modo de autenticación configurado en la aplicación Flask.
            if app.config['AUTHENTICATION_MODE'].lower() == 'masteruser':
                # En el modo 'masteruser', se utiliza una aplicación de cliente público.
                clientapp = msal.PublicClientApplication(app.config['CLIENT_ID'], authority=app.config['AUTHORITY_URL'])
                accounts = clientapp.get_accounts(username=app.config['POWER_BI_USER'])

                if accounts:
                    # Intenta recuperar un token de acceso desde la caché de usuario si está disponible.
                    response = clientapp.acquire_token_silent(app.config['SCOPE_BASE'], account=accounts[0])

                if not response:
                    # Si el token de acceso no está en caché, se realiza una llamada al cliente para obtenerlo
                    response = clientapp.acquire_token_by_username_password(app.config['POWER_BI_USER'], app.config['POWER_BI_PASS'], scopes=app.config['SCOPE_BASE'])

            # La autenticación del 'serviceprincipal' es recomendada por Microsoft para la inserción de Power BI en aplicaciones propias.
            elif app.config['AUTHENTICATION_MODE'].lower() == 'serviceprincipal':
                authority = app.config['AUTHORITY_URL'].replace('organizations', app.config['TENANT_ID'])
                clientapp = msal.ConfidentialClientApplication(app.config['CLIENT_ID'], client_credential=app.config['CLIENT_SECRET'], authority=authority)

                # Realiza una llamada al cliente para obtener el token de acceso.
                response = clientapp.acquire_token_for_client(scopes=app.config['SCOPE_BASE'])

            try:
                return response['access_token']  # Devuelve el token de acceso obtenido.
            except KeyError:
                raise Exception(response['error_description'])

        except Exception as ex:
            raise Exception('Error al obtener el token de acceso\n' + str(ex))
