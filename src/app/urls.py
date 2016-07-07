from django.conf.urls import patterns, include, url

from django.contrib import admin

from app.users.views import index

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r"^$", index, name="index"),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve'),
)
