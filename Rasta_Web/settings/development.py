from Rasta_Web.settings.base import *
import sys

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b-42%)g&&-uz(qo!6lb(273&2vc99s_xzqgu1)@0_tta@l@52g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'rasta_problem_bank': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
#
# TESTING = sys.argv[1] == 'test'
# # TESTING = True
# REGISTRATION_FEE = get_environment_var('REGISTRATION_FEE', '500')

