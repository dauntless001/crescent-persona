from persona.settings.packages.aws import *
from persona.settings.base import *
import os, dj_database_url



INSTALLED_APPS.append('storages')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY') 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False') == 'True'
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

MIDDLEWARE.insert(2, "whitenoise.middleware.WhiteNoiseMiddleware")

DATABASES['default'] = dj_database_url.parse(url=os.getenv('DATABASE_URL'), conn_max_age=600)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_DIRS = Path.cwd().joinpath(BASE_DIR).joinpath('faceApp/assets')
STATICFILES_DIRS = [
    STATIC_DIRS,
]

STATIC_ROOT = Path.cwd().joinpath(BASE_DIR).joinpath('assets')

#Media File
MEDIA_URL = '/media/'
MEDIA_ROOT = Path.cwd().joinpath(BASE_DIR).joinpath('faceApp/media')