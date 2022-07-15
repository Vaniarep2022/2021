from django.urls import path
from . import views

urlpatterns = [
    path('blog_detail/', views.blog_detail),
    path('blog_index/', views.blog_index, name ='reversed'),
]