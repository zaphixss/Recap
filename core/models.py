from django.db import models
from userauths import models as userauths_models
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)

    def __str__(self):
        return self.title  

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    views = models.IntegerField(default=0, blank=True, null=True)
    likes = models.IntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='image')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey( "core.Author" , on_delete=models.SET_NULL, null=True)

class Author(models.Model):
    fullname = models.CharField(max_length=100)
    headline = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image')
    youtube = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    user = models.ForeignKey(userauths_models.User, on_delete=models.SET_NULL, null=True)

class Comment(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    message = models.TextField(blank=True, null=True)
    save_info = models.BooleanField(default=False)
    count = models.IntegerField(default=0, blank=True, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name="comment")
    created_at = models.DateTimeField(auto_now_add=True)
