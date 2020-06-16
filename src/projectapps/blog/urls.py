from . import views
from django.urls import path

urlpatterns = [
    path('', views.blog, name='blogindex'), #Toni added view.blog whilst trying to link to the blog page
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail')

]
