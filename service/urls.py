__author__ = 'jc.cerquera10@uniandes.edu.co'
from service.views import UrlsViewSet, ContactViewSet
from rest_framework import routers
from django.conf.urls import include, url
from django.contrib import admin

# Determina la configuracion de la URL
router = routers.DefaultRouter()
router.register(r'urls', UrlsViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]