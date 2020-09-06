from django.urls import path,re_path,register_converter
from . import views,converters

register_converter(converters.FourDigitYearConverter,'yyyy')
urlpatterns = [
    path('',views.estimate_url),
    # path('test', views.book),
    # path('<str:name>',views.name),
    path('<str:name>',views.request_url),
]