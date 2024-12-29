from django.urls import path
from .views import TestView, CreatePostView

urlpatterns = [
    path('test/', TestView.as_view(), name='test'),
    path('create-post/', CreatePostView.as_view(), name='create-post'),
] 