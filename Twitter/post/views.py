from django.shortcuts import render, HttpResponse,get_object_or_404, HttpResponseRedirect,redirect, Http404
from .models import Post
from .forms import PostForm, CommentForm
from  django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

from django.utils.text import slugify
# Create your views here.

def post_index(request):
    posts_list = Post.objects.all()

    query = request.GET.get('q')
    if query:
        posts_list = posts_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(user__first_name__icontains=query)|
            Q(user__last_name__icontains=query)
        ).distinct()

    paginator = Paginator(posts_list, 3)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)


    return render(request,'post/index.html', {'posts':posts})
def post_detail(request,slug):
    post = get_object_or_404(Post,slug=slug)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'post': post,
        'form': form,

    }

    return render(request,'post/detail.html',context )
def post_create(request):

    if not request.user.is_authenticated:
        raise Http404()

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request, 'Başarlı Bir Şekilde Oluşturdunuz')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request,'post/form.html', context)

def post_update(request, slug):
    if not request.user.is_authenticated:
        raise Http404()

    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Başarlı Bir Şekilde Güncellediniz')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request,'post/form.html', context)
def post_delete(request,slug):
    if not request.user.is_authenticated:
        raise Http404()
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'Başarlı Bir Şekilde Sildiniz')
    return redirect('post:index')