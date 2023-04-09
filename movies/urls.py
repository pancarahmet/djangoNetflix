from django.urls import path
from .views import *


urlpatterns = [
    path('browse-index',browse_index,name="browse-index"),
]
