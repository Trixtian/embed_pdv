# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license

class ReportConfig:

    # Camel casing se utiliza para los miembros de variables ya que serán serializados y el formato camel case es estándar para las claves JSON

    reportId = None  # Identificador del informe
    reportName = None  # Nombre del informe
    embedUrl = None  # URL de incrustación del informe
    datasetId = None  # Identificador del conjunto de datos (opcional)

    def __init__(self, report_id, report_name, embed_url, dataset_id=None):
        self.reportId = report_id
        self.reportName = report_name
        self.embedUrl = embed_url
        self.datasetId = dataset_id
