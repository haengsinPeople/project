from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_main, name='post_main'),
    url(r'^explanation/$', views.post_explain, name='post_explain'),
    url(r'game/(?P<num>[0-9]+)/$', views.post_game, name='post_game'),
]
	