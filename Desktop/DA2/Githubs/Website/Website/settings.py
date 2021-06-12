
from pathlib import Path
import os
from django.conf import settings
from django.core.mail import send_mail

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '9z+%sy87ib$o)a(#jck#_&_^#0=o=cvzh+m__bq9ai0w#d_8wj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'Home',
    'Users',
    'Contents',
    'pwa',
    'django_extensions',


    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'Home')], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'Website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'shopshoes',

        'USER': 'postgres',

        'PASSWORD': '123456',

        'HOST': 'localhost',

        'PORT': '5432',

    }

}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST ='smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'thinhphamndtdtu@gmail.com'
EMAIL_HOST_PASSWORD ='laptrinhc2801'
MAIL_USERNAME='thinhphamndtdtu@gmail.com'
# MAIL_USERNAME='dinhquangtrung0613968396@gmail.com'
EMAIL_USE_TLS = True #Cài đặt này chỉ định liệu Email có sử dụng kết nối TLS hay không
DEFAULT_FROM_EMAIL = 'thinhphamndtdtu@gmail.com'




# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]

LOGIN_REDIRECT_URL = 'Contents:contents'
LOGIN_URL = 'login'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

PWA_APP_NAME = "ShopeShoes"
PWA_APP_DESCRIPTION = "Aplication have service worker product by my team in TDT go finishing in Schools"
PWA_APP_THEME_COLOR = "#3477f5"
PWA_APP_BACKGROUND_COLOR = "#6699f7"

PWA_APP_ICONS = [
	{
		"src": "/static/Home/img/header/logo4.jpg",
		"sizes":"160x160"
	}
]

PWA_APP_ICONS_APPLE = [
	{
		"src": "/static/Home/img/header/logo4.jpg",
		"sizes": "160x160"
	}
]

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR,"serviceworker.js")

GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}