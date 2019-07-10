from .base import *
import os

ALLOWED_HOSTS = ['*youths-world.herokuapp.com']

DEBUG = os.environ.get('DEBUG', False)

try:
    from .local import *
except ImportError:
    pass
