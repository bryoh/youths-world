from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', True)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vr8oz8=5^dw-bkmundzpej-_bkz%tasmwcrlq2i05dlv!hpel_'
ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', 'youths-world.herokuapp.com']


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
