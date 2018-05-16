from django.shortcuts import render,get_object_or_404,redirect
from myApp.models import Blog
from myApp.forms import BlogForm
from django.utils import timezone

def index(request):
    args = {
        'insert':'Ringed Planet Somewhere in Space maybe, also a Dictionary key',
        'insert2':'I am the second insert dictionary key',
        'insert3':'Third dictionary insertion point',}
    return render(request, 'myApp/index.html',context=args)

def post_list(request):
    post = Blog.objects.order_by('created')
    args = {'post':post}
    return render(request, 'myApp/post_list.html',context=args)

def post_detail(request, pk):
    detail = get_object_or_404(Blog, pk=pk)
    return render(request, 'myApp/post_detail.html',{'detail':detail})

def post_new(request):
    if request.method =='POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.time = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = BlogForm()
    return render(request,'myApp/post_new.html',{'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.time = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = BlogForm(instance=post)
    return render(request,'myApp/post_edit.html',{'form':form})
