from .base import *

SECRET_KEY = 'django-insecure-e6#zz@kcy7a+6_4@63@q(xvpkkkb1nq_39=6jv&1e@4o&c0w^v'

DEBUG = True

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR),"static"),
)

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'informatorio',
        'USER': 'sa',
        'PASSWORD': 'sa',
        'HOST': 'PHILIPPE\SQLEXPRESS',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        }
    }
}