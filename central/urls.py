

from django.urls import path
from .views import homepage_central

urlpatterns = [
    path('', homepage_central, name="home-central"),

]
