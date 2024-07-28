from django.urls import path
from blog.views import BlogListView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('blog_list/', BlogListView.as_view(), name='blog-list'),
    path('blog_detail/', BlogDetailView.as_view(), name='blog-detail'),
]
