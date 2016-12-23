from django.conf.urls import url
from . import views
from lab.views import CarView, AddressView, SalesView, UserView


urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^model_row$', CarView.as_view(), name='model_row'),
    url(r'^sales$', SalesView.as_view(), name='sales'),
    url(r'^users$', UserView.as_view(), name='users'),
    url(r'^address$', AddressView.as_view(), name='address'),

    ]
