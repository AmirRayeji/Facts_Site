from  django.urls import path
from . import views

urlpatterns=[
    path('',views.PostListView.as_view(), name='post_list'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('facts/create/', views.PostCreateView.as_view(), name='post_create'),
]