import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Set DEBUG to False in production
DEBUG = True

SECRET_KEY = '&a@f(0@lrl%606smticbu20=pvribdvubk5=gjti8&n1y%bi&4'

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'openwisp_utils.admin_theme',
    # all-auth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # rest framework
    'rest_framework',
    'django_filters',
    # registration
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    # social login
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    # openwisp2 modules
    'openwisp_users',
    'openwisp_radius',
    # admin
    'django.contrib.admin',
]

EXTENDED_APPS = ['django_freeradius']
LOGIN_REDIRECT_URL = 'admin:index'

AUTH_USER_MODEL = 'openwisp_users.User'
SITE_ID = '1'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'openwisp_utils.staticfiles.DependencyFinder',
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

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'openwisp_utils.loaders.DependencyLoader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'openwisp_radius.db'),
    }
}

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

# WARNING: for development only!
AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'Europe/Rome'
USE_I18N = False
USE_L10N = False
USE_TZ = True
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
EMAIL_PORT = '1025'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

# for development only
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Swapper model definitions
DJANGO_FREERADIUS_RADIUSREPLY_MODEL = 'openwisp_radius.RadiusReply'
DJANGO_FREERADIUS_RADIUSGROUPREPLY_MODEL = 'openwisp_radius.RadiusGroupReply'
DJANGO_FREERADIUS_RADIUSCHECK_MODEL = 'openwisp_radius.RadiusCheck'
DJANGO_FREERADIUS_RADIUSGROUPCHECK_MODEL = 'openwisp_radius.RadiusGroupCheck'
DJANGO_FREERADIUS_RADIUSACCOUNTING_MODEL = 'openwisp_radius.RadiusAccounting'
DJANGO_FREERADIUS_NAS_MODEL = 'openwisp_radius.Nas'
DJANGO_FREERADIUS_RADIUSUSERGROUP_MODEL = 'openwisp_radius.RadiusUserGroup'
DJANGO_FREERADIUS_RADIUSPOSTAUTH_MODEL = 'openwisp_radius.RadiusPostAuth'
DJANGO_FREERADIUS_RADIUSBATCH_MODEL = 'openwisp_radius.RadiusBatch'
DJANGO_FREERADIUS_RADIUSGROUP_MODEL = 'openwisp_radius.RadiusGroup'

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
        ],
        'VERIFIED_EMAIL': True,
    },
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# local settings must be imported before test runner otherwise they'll be ignored
try:
    from local_settings import *
except ImportError:
    pass
