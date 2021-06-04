SECRET_KEY = 'secret-key'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'db_user',
        'HOST': 'localhost',
        'PASSWORD': 'db_password',
        'PORT': 5432
    }
}

EMAIL_USE_TLS = True
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
