from .base import *

ALLOWED_HOSTS = ['localhost']

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
