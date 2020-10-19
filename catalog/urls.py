from django.urls import path
from . import views

urlpatterns = [
    # TODO: convert this to a class based view.
    path('', views.index, name='index'),
]
