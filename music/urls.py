from . import views
from django.urls import path
from django.conf.urls import url

app_name = 'music'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:album_id>/', views.detail, name='detail'),
]