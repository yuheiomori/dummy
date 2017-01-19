from django.template.response import TemplateResponse, HttpResponse
import logging

from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def bounce(request):
    logger.debug('bounce')
    logger.debug(request.META)
    logger.debug(request.GET)
    logger.debug(request.POST)
    logger.debug(request.body)

    return TemplateResponse(request, 'bounce.html', {})


@csrf_exempt
def complaint(request):
    logger.debug('complaint')
    logger.debug(request.META)
    logger.debug(request.GET)
    logger.debug(request.POST)
    logger.debug(request.body)
    return TemplateResponse(request, 'complaint.html', {})
