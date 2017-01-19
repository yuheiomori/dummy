from django.template.response import TemplateResponse, HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('index access')
    return TemplateResponse(request, 'index.html', {})


def namahage(request):
    return TemplateResponse(request, 'namahage.html', {})


def ogp(request, original_path):

    logger.debug('ogp access')
    logger.debug(request.META)
    logger.debug(request.GET)
    logger.debug(original_path)
    return TemplateResponse(request, 'ogp.html', {})


def bounce(request):
    logger.debug('bounce')
    logger.debug(request.META)
    logger.debug(request.GET)
    logger.debug(request.POST)

    return TemplateResponse(request, 'bounce.html', {})


def complaint(request):
    logger.debug('complaint')
    logger.debug(request.META)
    logger.debug(request.GET)
    logger.debug(request.POST)
    return TemplateResponse(request, 'complaint.html', {})
