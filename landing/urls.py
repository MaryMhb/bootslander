from django.urls import path
from django.conf.urls.static import static
from landing.views import *

urlpatterns = [
    path('', index_view )
]
