from django.urls import path
from Jing import views
app_name = 'Jing'
urlpatterns = [
path('', views.index, name='index'),
]