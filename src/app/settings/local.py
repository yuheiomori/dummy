from .settings import *

LOG_DIR = '/tmp/sandbox/'
ALLOWED_HOSTS = ['*']
LOGGING = {}
STATICFILES_DIRS = (
    os.path.join(REPOSITORY_ROOT, 'static'),
)
