from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list$', views.list_correo),
    url(r'^new$', views.new_correo),
]
