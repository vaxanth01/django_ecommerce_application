from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-ec65z229mhfzv8ofg4+jfwy2*bh+tdkold5&((tc7$8+5k!sh-'
DEBUG = True
ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.1.16']
# ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.1.32']
# ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.0.118']
# ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.0.106']
# ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.1.25']
# ALLOWED_HOSTS = ['localhost', '127.0.0.1' , '192.168.230.145']

# In your settings.py

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'  # Replace with your SMTP server hostname or IP address
EMAIL_PORT = 587  # Adjust the port if necessary, default is 587 for TLS
EMAIL_USE_TLS = True  # Set to True if your SMTP server requires TLS, False otherwise
EMAIL_HOST_USER = 'vaxanth01@gmail.com'  # Your SMTP username
EMAIL_HOST_PASSWORD = 'vaxanth'  # Your SMTP password


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'app',
    'category',
    'store',
    'cart',
    'accounts',
    'orders',
    'addproduct',
    'sslserver',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'category.context_processors.menu_links',
                'cart.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'
AUTH_USER_MODEL = 'app.Account'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'ecommerce',
		'USER': 'root',
		'PASSWORD': '',
		'HOST':'localhost',
		'PORT':'3306',
        'OPTIONS': {
            'sql_mode': 'STRICT_TRANS_TABLES',
        },
	}
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'ecommerce',
#         'USER': 'root',
#         'PASSWORD': 'itsol@2016',
#         'HOST': '192.168.1.10',
#         'PORT': '3306',
#     }
# }


AUTH_PASSWORD_VALIDATORS = []


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
# myproject/settings.py
# AUTH_USER_MODEL = 'user.Management'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/meida/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'meida')
CRISPY_TEMPLATE_PACK = 'bootstrap4'

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',

    
}


# settings.py

STRIPE_PUBLISHABLE_KEY = 'your_stripe_publishable_key'
STRIPE_SECRET_KEY = 'your_stripe_secret_key'
