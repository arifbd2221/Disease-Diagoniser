from django.urls import path
from .views import *
urlpatterns = [
    path('myadmin/', myadmin, name='admin'),
    path('register/doctor/', addDoctor, name='addoctor'),
    path('details/doctor/<int:id>', detailsDoctor, name='detailsdoctor'),
    path('delete/doctor/<int:id>/', deleteDoctor, name='deletedoctor'),
    path('update/doctor/<int:id>/', editDoctor, name='editdoctor'),
]