from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^partes/(?P<curso>[0-9]+)$', views.imprimir_partes),
	url(r'^show/(?P<tipo>[a-z]+)/(?P<mes>[0-9]+)/(?P<ano>[0-9]+)/(?P<dia>[0-9]+)$', views.imprimir_show),
	url(r'^carta_amonestacion/(?P<mes>[0-9]+)/(?P<ano>[0-9]+)/(?P<dia>[0-9]+)$', views.carta_amonestacion),
	url(r'^carta_sancion/(?P<identificador>[0-9]+)$', views.carta_sancion),
]