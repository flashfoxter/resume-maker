from django.urls import path
from . views import resume, final
urlpatterns = [
    path('resume/', resume, name='resume'),
    path('final/', final, name='final')
]