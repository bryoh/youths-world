from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vr8oz8=5^dw-bkmundzpej-_bkz%tasmwcrlq2i05dlv!hpel_'
ALLOWED_HOSTS = ['*youths-world.herokuapp.com', 'localhost']


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
