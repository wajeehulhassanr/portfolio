"""
WSGI config for portfolio project.
"""

import os
import sys
import logging
from django.core.wsgi import get_wsgi_application

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
    application = get_wsgi_application()
    logger.info("WSGI application initialized successfully.")
except Exception as e:
    logger.error("Failed to initialize WSGI application: %s", e)
    sys.exit(1)  # Exit if the application fails to start