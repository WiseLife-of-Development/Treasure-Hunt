from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.utils import timezone
from .forms import BlogForm
# Create your views here.

def home(request):
    health = Health.objects.all()
    return render(request,'home.html',{'health' : health})

def detail(request,id):
    health = get_object_or_404(Health,pk = id)  #id값의 블로그를 가져오거나 404
    return render(request,'detail.html',{'health':health})

def new(request):
    form = HealthForm()
    return render(request,'new.html',{'form':form})

def create(request):
    form = HealthForm(request.POST,request.FILES)
    if form.is_valid():
        new_health = form.save(commit=False)
        new_health.pub_data = timezone.now()
        new_health.save()
        return redirect('detail',new_health.id)
    return redirect('home')

def edit(request,id):
    edit_health = Health.objects.get(id=id)
    return render(request,'edit.html',{'blog':edit_health})

def update(request,id):
    update_health = Health.objects.get(id=id)
    update_health = request.POST['title']
    update_health.title = request.POST['title']
    update_health.writer = request.POST['writer']
    update_health.body = request.POST['body']
    update_health.pub_data = timezone.now()
    update_health.save()
    return redirect('detail',update_health.id)

def delete(request,id):
    delete_blog = Health.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')