from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('detail/<int:page_id>/', detail, name="youtuber_detail"),
]
