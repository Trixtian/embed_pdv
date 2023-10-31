# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'ServicePrincipal'

    # Workspace Id in which the report is present
    WORKSPACE_ID = '9f1968f6-3857-465b-b112-aef5423f4bb0'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = 'b15990ed-20e5-4154-941c-467ee2f36945'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = '642f4ac0-9138-468d-82bf-ef1b80d3ab21'
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = '13839295-2c2c-4884-99d2-8bdbd467f7be'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = 'dZB8Q~yHXN.NUKxsaGl6mbt6JXcEfD~s~F3h4dxl'
    
    # Scope Base of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE_BASE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY_URL = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = ''
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = ''