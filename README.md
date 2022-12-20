"# proyecto_informatorio" 
GRUPO: 2

INTEGRANTES: 
    Aranda Celeste
    Brunelli Antonella
    Ledesma Ramiro
    Martinez Manuel 
    Maurel Damián
    Mesa Ruth
    Peralta Federico


Crear un archivo local.py al mismo nivel que base.py en settings con la siguiente estructura:
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': config('NAME'),
        'USER': config('USER'),
        'PASSWORD': config('PASSWORD'),
        'HOST': config('HOST'),
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        }
    }
}