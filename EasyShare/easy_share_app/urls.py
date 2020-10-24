from django.urls import path
from .views import home_page, download

urlpatterns = [
   path('',home_page, name='home_page'),
   path('download/',download)
]
