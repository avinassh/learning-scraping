from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /challenge/7/
    url(r'^challenge/(7?P<challenge_id>[0-9]+)/$', views.challenge, name='challenge'),
    # ex: /solution/9/
    url(r'^solution/(?P<challenge_id>[0-9]+)/$', views.solution, name='solution'),
    # ex: /api/1/
    url(r'^api/(?P<challenge_id>[0-9]+)/$', views.api, name='api'),
]