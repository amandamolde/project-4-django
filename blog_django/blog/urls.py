from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.DetailPost.as_view()),
    path('<int:pk>/comments/', views.CommentList.as_view()),
    path('<int:pk>/comments/<int:pk>/', views.CommentDetail.as_view()),
]