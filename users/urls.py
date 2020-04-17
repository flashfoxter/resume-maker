from django.urls import path
from . views import home, register
urlpatterns = [
    path('', home),
    path('signup', register, name='register')
]