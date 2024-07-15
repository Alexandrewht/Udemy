from django.urls import path
from . import views

app_name = 'blog'

# Blog/
# Django urls:
# https://docs.djangoproject.com/en/5.0/topics/http/urls/
urlpatterns = [
    path('', views.blog, name='home'),
    # path('post/', views.blog, name='blog'),
    path('<int:post_id>/', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
