from pathlib import Path
from .base import *
import os
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#La base de datos del proyecto general y el de pruebas local deberia de ser diferente 
#Tambien deberia de ser diferente las ip permitidas para que accedan al proyectok
DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('db.sqlite3'),
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
STATIC_URL = '/static/'
STATICFILES_DIRS =[BASE_DIR.child('static')]