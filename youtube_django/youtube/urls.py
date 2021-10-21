from django.urls import path
from . import views

urlpatterns = [
    path('comments/<str:video>/', views.CommentList.as_view()),
    path('comment/<int:pk>/', views.CommentDetail.as_view()),
    path('replies/<int:comment>', views.ReplyList.as_view()),
    path('comment/<int:pk>/reply', views.ReplyDetail.as_view()),
    path('comments/<int:pk>/thumbs_up', views.CommentLikes.as_view()),
    path('comments/<int:pk>/thumbs_down', views.CommentLikes.as_view()),
    path('comments/reply/<int:comment>', views.ReplyList.as_view()),
    path('commentsection/<str:video>/', views.CommentSection.as_view()),
]