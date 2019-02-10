from .views import *
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('', Index.as_view(), name= 'index'),
    path('<int:pk>/', Detail.as_view(), name= 'detail'),
    path('posting/', Posting.as_view(), name= 'postiong')
]