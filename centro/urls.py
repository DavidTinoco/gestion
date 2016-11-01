from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^alumnos$', views.alumnos),
    url(r'^profesores/change/(?P<campo>[A-Za-z]+)/(?P<codigo>[0-9]+)/(?P<operacion>[a-z]+)$', views.profesores_change),
    url(r'^profesores$', views.profesores),
    
    
]