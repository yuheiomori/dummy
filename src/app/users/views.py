from django.template.response import TemplateResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('index access')
    return TemplateResponse(request, 'index.html', {})
