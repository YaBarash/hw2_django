from django.urls import path
from catalog.apps import DjangoProjectConfig
from catalog.views import home, contacts

app_name = DjangoProjectConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts')
]