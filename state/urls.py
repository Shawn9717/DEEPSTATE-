from unicodedata import name
from django.conf import path
from . import views

urlpatterns = [
    path('landing/',views.landing,name='landing'),
    path('date_today/',views.date_today, name = "date_today"),
]


