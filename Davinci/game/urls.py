from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_main, name='post_main'),
    url(r'^explanation/$', views.post_explain, name='post_explain'),
    url(r'^game/$', views.post_stay, name='post_stay'),
    url(r'^game/(?P<name>[0-9]+)/$', views.post_game, name='post_game'),
]
	