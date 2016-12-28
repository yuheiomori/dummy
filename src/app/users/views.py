from django.template.response import TemplateResponse, HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('index access')
    return TemplateResponse(request, 'index.html', {})


def namahage(request):
    return TemplateResponse(request, 'namahage.html', {})


def ogp(request):
    logger.debug('ogp access')
    logger.debug(request.META)
    logger.debug(request.GET)
    return HttpResponse('<marquee>Hello hello hello how low</marquee>', {})
