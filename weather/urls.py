from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.weather,name="weather"),
    path('delete/<int:id>',views.delete_item,name="delete_item"),
]