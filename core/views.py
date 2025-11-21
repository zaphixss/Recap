from django.shortcuts import render, redirect
from .models import Category, Author, Comment, Blog
from userauths.models import User
from django.contrib.auth.decorators import login_required
from .forms import BlogForm, AuthorForm

# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    context= {
        'blogs':blogs
    }
    return render(request, 'index.html', context)

def category(request):
    category = Category.objects.all()

    context = {
        'category':category
    }
    return render(request, 'category.html', context)

def category_detail(request, id):
    category = Category.objects.get(id=id)
    blogs = Blog.objects.filter(category=category)
    context = {
        'blogs': blogs,
        'category': category
    }
    return render(request, 'category_detail.html', context)

def authors(request):
    author = Author.objects.all()
    context = {
        'author': author
    }
    return render(request,'writers/author.html',context)

def author_detail(request, username):
    user = User.objects.get(username=username)
    author = Author.objects.get(user=user)
    blogs = Blog.objects.filter(author=author)

    context = {
        'blogs': blogs,
        'author': author
    }
    return render(request, 'writers/author_detail.html', context)


def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    blogs = Blog.objects.all()
    comments = Comment.objects.filter(blog=blog)

    context = {
        'blog': blog,
        'blogs': blogs,
        'comments': comments
    }
    return render(request, 'blog_detail.html', context)

def comment(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        save = "save" in request.POST

        Comment.objects.create(
            fullname = name,
            email = email,
            message = message,
            save_info = save,
            blog = blog
        )

        return redirect('blog_detail', id)
@login_required
def home(request,):
    author = Author.objects.get(user=request.user)
    blogs = Blog.objects.filter(author=author)
    comments = Comment.objects.filter(blog__author=author)

    context={
        'blogs':blogs,
        'author':author,
        'comments':comments
        
    }
    return render(request, 'dashboard/home.html', context)



def dashboard_comments(request):
    author = Author.objects.get(user=request.user)
    blogs = Blog.objects.filter(author=author)
    comments = Comment.objects.filter(blog__author=author)

    context = {
        'author':author,
        'blogs':blogs,
        'comments':comments
    }

    return render(request, 'dashboard/comments.html', context)


def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            blog = form.save(commit=False)                  
            blog.author = Author.objects.get(user=request.user)  
            blog.save()
            return redirect("dashboard_home")

    else:
        form = BlogForm()

    context = {"form": form}
    return render(request, "dashboard/add_blog.html", context)

def blog_delete(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('dashboard_home')

def blog_update(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)    
        if form.is_valid():
            blog = form.save()
            return redirect('dashboard_home')
    else:
        form = BlogForm(instance=blog)

    context ={
        'form': form,
        'blog': blog
    }        
    return render(request,'dashboard/blog_update.html', context)

def settings(request):
    author = Author.objects.get(user= request.user)
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect('settings')
    else:
        form = AuthorForm(instance=author)
    context= {
        'form':form
    }
    return render(request,'dashboard/settings.html', context)        