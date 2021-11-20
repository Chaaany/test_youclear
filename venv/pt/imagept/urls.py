from django.urls import path
from .views import *

urlpatterns = [
    path('image/<int:page_id>', image),
    path('playlist/', playlist),
    path('signin/', signin),
    path('signup/', signup),
]
