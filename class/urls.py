

from django.urls import path
from .views import *

urlpatterns = [
    path('homepage/', home_view, name='home_view'),
    path('', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('professor/', professor_dashboard, name='professor_dashboard'),

    # Additional URL patterns for other views if needed
]
