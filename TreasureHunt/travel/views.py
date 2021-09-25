from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm
# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    return render(request,'home.html',{'blogs' : blogs})

def detail(request,id):
    blog = get_object_or_404(Blog,pk = id)  #id값의 블로그를 가져오거나 404
    return render(request,'detail.html',{'blog':blog})

def new(request):
    form = BlogForm()
    return render(request,'new.html',{'form':form})

def create(request):
    form = BlogForm(request.POST,request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.pub_data = timezone.now()
        new_blog.save()
        return redirect('detail',new_blog.id)
    return redirect('home')

def edit(request,id):
    edit_blog = Blog.objects.get(id=id)
    return render(request,'edit.html',{'blog':edit_blog})

def update(request,id):
    update_blog = Blog.objects.get(id=id)
    update_blog = request.POST['title']
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_data = timezone.now()
    update_blog.save()
    return redirect('detail',update_blog.id)

def delete(request,id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')

def search(request):
    search_keyword = request.GET.get('q')

    if len(search_keyword) >= 1:
        rental_list = Health.objects.filter(product=search_keyword)

    else:
        rental_list = Health.objects.all()

    return render(request, 'rental.html', {
        'rentals': rental_list
    })