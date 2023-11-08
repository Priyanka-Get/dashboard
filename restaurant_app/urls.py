from .import views
from django.urls import path

urlpatterns = [
   path('base/',views.base,name='dashboard'),
   path('login/',views.login,name='login'),
]