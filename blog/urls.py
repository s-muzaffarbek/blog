from django.urls import path

from .views import BlogView, BlogCreateVeiw, BlogDetailView, BlogUpdateView, \
    BlogDeleteView, CategoryBlogView, CategoryView, TagView

urlpatterns = [
    path('', BlogView.as_view(), name='blog_list'),
    path('category/', CategoryView.as_view(), name='category_list'),
    path('detail/<slug:slug>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/<slug:slug>', CategoryBlogView.as_view(), name='blog_category'),
    path('update/<slug:slug>', BlogUpdateView.as_view(), name='blog_update'),
    path('create/', BlogCreateVeiw.as_view(), name='blog_create'),
    path('tag/<slug:slug>', TagView.as_view(), name='tag_filter'),
    path('delete/<slug:slug>', BlogDeleteView.as_view(), name='blog_delete'),
]
