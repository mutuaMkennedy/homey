import cloudinary
import cloudinary.uploader
import cloudinary.api
from homey.settings.base import *

# python manage.py runserver --settings=homey.settings.local

# Use when is running windows os
# if os.name == 'nt':
#     import platform
#     OSGEO4W = r'C:\OSGeo4W'
#     if '64' in platform.architecture()[0]:
#         OSGEO4W += '64'
#     assert os.path.isdir(OSGEO4W), 'Directory does not exist: ' + OSGEO4W
#     os.environ['OSGEO4W_ROOT'] = OSGEO4W
#     os.environ['GDAL_DATA'] = OSGEO4W + r'\share\gdal'
#     os.environ['PROJ_LIB'] = OSGEO4W + r'\share\proj'
#     os.environ['PATH'] = OSGEO4W + r'\bin;' + os.environ['PATH']


# GDAL_LIBRARY_PATH = r'C:\OSGeo4W64\bin\gdal202.dll'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD', cast=str),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

EMAIL_USE_TLS = config('EMAIL_USE_TLS',cast=bool)
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_SSL = config('EMAIL_USE_SSL', cast=bool)
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

#claudinary settings
cloudinary.config(
  cloud_name = config('CLOUD_NAME'),
  api_key = config('API_KEY'),
  api_secret = config('API_SECRET')
)
