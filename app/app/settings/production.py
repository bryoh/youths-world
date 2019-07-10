from .base import *

ALLOWED_HOSTS = ['*youths-world.herokuapp.com']

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
