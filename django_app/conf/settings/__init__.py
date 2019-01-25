from .base import *
from ._installed_apps import *
IS_PRODUCTION = os.environ.get('IS_PRODUCTION', False)

if IS_PRODUCTION:
    from .prod import *
    INSTALLED_APPS += PROD_APS
else:
    from .dev import *
    INSTALLED_APPS += DEV_APS
