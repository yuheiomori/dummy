from django.conf.urls import url, include


from django.contrib import admin
from django.views.static import serve

from app.users.views import index, namahage, ogp

admin.autodiscover()

urlpatterns = [
    url(r"^$", index, name="index"),
    url(r"^namahage/?$", namahage, name="namahage"),
    url(r"^ogp(?P<original_path>.*)$", ogp, name="ogp"),
    url(r"^namahage2/?$", namahage, name="namahage2"),
    url(r"^namahage3/?$", namahage, name="namahage3"),
    url(r'^bouncy/?$', include('django_bouncy.urls')),
    url(r'^static/(?P<path>.*)$', serve),

]
