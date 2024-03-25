from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= 'index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('gallery', views.gallery, name= 'gallery'),
    path('blog/<int:pk>/', views.blog_detail, name='blogdetail'),
    path('services/', views.services, name='services')
]
