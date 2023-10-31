# Copyright (c) Microsoft Corporation.
# Licenciado bajo la licencia MIT

class EmbedToken:

    # Camel casing se utiliza para los miembros de variables ya que serán serializados y el formato camel case es estándar para las claves JSON

    tokenId = None  # Identificador del token
    token = None    # El token en sí
    tokenExpiry = None  # La fecha de vencimiento del token

    def __init__(self, token_id, token, token_expiry):
        """
        Constructor de la clase EmbedToken.

        Args:
            token_id (str): El identificador del token.
            token (str): El token en sí.
            token_expiry (str): La fecha de vencimiento del token.
        """
        self.tokenId = token_id
        self.token = token
        self.tokenExpiry = token_expiry
