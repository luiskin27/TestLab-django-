from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_list_view(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs, 'blog': blogs})

def blog_detail_view(request, id):
    blog = get_object_or_404(Blog, id=id)
    # добавлям +1 лайк
    blog.likes += 1
    blog.save()
    # передаем и blog_id и blog шоб все работало
    return render(request, 'blog_detail.html', {'blog_id': blog, 'blog': blog})