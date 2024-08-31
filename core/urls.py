from django.urls import path

from core.views import *


urlpatterns = [
    
    path('', base, name='base'),
    path('send_emaile',send_emaile, name='send_emaile'),
    path('thank_you',thank_you),
]
