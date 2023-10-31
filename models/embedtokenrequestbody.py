# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license

class EmbedTokenRequestBody:

    # Camel casing se utiliza para los miembros de variables ya que serán serializados y el formato camel case es estándar para las claves JSON

    datasets = None  # Listado de conjuntos de datos
    reports = None  # Listado de informes
    targetWorkspaces = None  # Listado de espacios de trabajo de destino

    def __init__(self):
        self.datasets = []  # Inicializa la lista de conjuntos de datos
        self.reports = []   # Inicializa la lista de informes
        self.targetWorkspaces = []  # Inicializa la lista de espacios de trabajo de destino
