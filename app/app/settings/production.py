from .base import *
import os

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', 'youths-world.herokuapp.com']
SECRET_KEY = os.environ.get('SECRET_KEY', '')
DEBUG = os.environ.get('DEBUG', False)

try:
    from .local import *
except ImportError:
    pass
