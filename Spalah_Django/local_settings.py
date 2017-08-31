import os

DEBUG = True

PROJ_MODULE_ROOT = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.normpath(os.path.join(PROJ_MODULE_ROOT, ".."))
root_path = lambda *args: os.path.join(ROOT, *args)
path = lambda *args: os.path.join(PROJ_MODULE_ROOT, *args)


MEDIA_ROOT = path('../..')
MEDIA_URL = '/media/'
STATIC_ROOT = path('../../static/')
STATIC_URL = '/static/'