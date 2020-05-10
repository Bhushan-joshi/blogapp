from django.urls import path
from .views import PostList,DetailView,CreatePost,UpdatePost,DeletePost
from . import views

urlpatterns = [
    #path('' , views.index , name='index'),
    path('' , PostList.as_view() , name='index'),
    path('post/<int:pk>/' , DetailView.as_view() , name='detail_view'),
    path('post/new/',CreatePost.as_view(),name='create_post'),
    path('post/<int:pk>/update/',UpdatePost.as_view(),name='update_post'),
    path('post/<int:pk>/delete/',DeletePost.as_view(),name='delete_post'),
    path('about/',views.about, name='about'),
   
]
