from django.conf.urls import patterns, include, url

from django.contrib import admin

from app.users.views import index, namahage, ogp, bounce, complaint

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r"^$", index, name="index"),
    url(r"^namahage?/$", namahage, name="namahage"),
    url(r"^ogp(?P<original_path>.*)$", ogp, name="ogp"),
    url(r"^namahage2?/$", namahage, name="namahage2"),
    url(r"^namahage3?/$", namahage, name="namahage3"),
    url(r"^bounce?/$", bounce, name="bounce"),
    url(r"^complaint?/$", complaint, name="complaint"),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve'),

)
