import cloudinary
import cloudinary.uploader
import cloudinary.api
from homey.settings.base import *
from glob import glob

GDAL_LIBRARY_PATH=glob('/usr/lib/libgdal.so.*')[0]
GEOS_LIBRARY_PATH=glob('/usr/lib/libgeos_c.so.*')[0]

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),

    }
    
}

STATICFILES_STORAGE = 'homey.storage.ForgivingManifestStaticFilesStorage'

EMAIL_USE_TLS = config('EMAIL_USE_TLS',cast=bool)
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_SSL = config('EMAIL_USE_SSL',cast=bool)
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

#cludinary settings
cloudinary.config(
  cloud_name = config('CLOUD_NAME'),
  api_key = config('API_KEY'),
  api_secret = config('API_SECRET')
)

# Sentry configuration
sentry_sdk.init(
    dsn= config('SENTRY_DSN'),
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
