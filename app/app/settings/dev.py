from .base import *

DEBUG = True

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', None)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
if AWS_ACCESS_KEY_ID is not None:
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_DEFAULT_ACL = None
    AWS_LOCATION = 'static'
    AWS_S3_FILE_OVERWRITE = False

    STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    MEDIA_URL = 'https://%s/%s/media/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
else:
    STATICFILES_FINDERS = ['django.contrib.staticfiles.finders.FileSystemFinder', 'django.contrib.staticfiles.finders.AppDirectoriesFinder']
    STATICFILES_DIRS = [os.path.join(PROJECT_DIR, 'static')]

    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'

INSTALLED_APPS = INSTALLED_APPS + ['debug_toolbar']
MIDDLEWARE = MIDDLEWARE + ['debug_toolbar.middleware.DebugToolbarMiddleware']

# INTERNAL_IPS = ("127.0.0.1", "172.17.0.1")

try:
    from .local import *
except ImportError:
    pass
