# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license

class EmbedConfig:

    # Camel casing se utiliza para los miembros de variables ya que serán serializados y el formato camel case es estándar para las claves JSON

    tokenId = None  # Identificador del token
    accessToken = None  # Token de acceso
    tokenExpiry = None  # Fecha de vencimiento del token
    reportConfig = None  # Configuración del informe

    def __init__(self, token_id, access_token, token_expiry, report_config):
        """
        Constructor de la clase EmbedConfig.

        Args:
            token_id (str): El identificador del token.
            access_token (str): El token de acceso.
            token_expiry (str): La fecha de vencimiento del token.
            report_config (str): La configuración del informe.
        """
        self.tokenId = token_id
        self.accessToken = access_token
        self.tokenExpiry = token_expiry
        self.reportConfig = report_config
