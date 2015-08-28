from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /challenge/7/
    url(r'^challenge/(?P<challenge_id>[0-9]+)/$', views.challenge,
        name='challenge'),
    # ex: /solution/9/
    url(r'^solution/(?P<challenge_id>[0-9]+)/$', views.solution,
        name='solution'),
    # ex: /api/1/
    url(r'^api/(?P<challenge_id>[0-9]+)/$', views.api, name='api'),
    # ex: /login
    url(r'^login/$', views.user_login, name='user_login'),
    # ex: /logout
    url(r'^logout/$', views.user_logout, name='user_logout'),
    # ex: /signup
    url(r'^signup/$', views.signup, name='signup'),
    # ex: /keys
    url(r'^keys/$', views.keys, name='keys'),
]
