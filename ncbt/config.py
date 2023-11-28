from pathlib import Path
DEBUG = False
ROOT = Path.home()
DOMAIN_ROOT = 'ncbt.info'
SITE_URL = 'https://ncbt.info'

if DEBUG:
    SITE_URL = ''