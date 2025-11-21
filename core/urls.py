from django.urls import path
from core import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category/detail/<id>/", views.category_detail, name="detail"),
    path("authors/", views.authors, name="authors"),
    path("author/detail/<username>/", views.author_detail, name="author_detail"),
    path("blog/detail/<id>/", views.blog_detail, name="blog_detail"),
    path("category/", views.category, name="category"),
    path("comment/<id>/", views.comment, name="comment"),
    path("dashboard/home/", views.home, name="dashboard_home"),
    path("dashboard/comments/", views.dashboard_comments, name="dashboard_comments"),
    path("dashboard/add/", views.add_blog, name="add_blog"),
    path("dashboard/delete/<id>/", views.blog_delete, name="blog_delete"),
    path("dashboard/update/<id>/", views.blog_update, name="blog_update"),
    path("dashboard/settings/", views.settings, name="settings"),
]