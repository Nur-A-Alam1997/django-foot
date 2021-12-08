from django.urls import path
from . import views

urlpatterns =[
    path("welcome",views.welcome),
    path("template",views.template)
]