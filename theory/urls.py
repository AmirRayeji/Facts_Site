from  django.urls import path

from theory import views


urlpatterns=[
    path('',views.PostListView.as_view(), name='post_list'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('facts/create/', views.PostCreateView.as_view(), name='post_create'),
    path('facts/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('facts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]