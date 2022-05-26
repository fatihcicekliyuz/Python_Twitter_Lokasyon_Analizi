from django.shortcuts import render

import sys
import os

from post.models import Post

# Create your views here.



def home_view(request):
    posts_list = Post.objects.all()
    print(len(posts_list))
    if request.user.is_authenticated:

        context = {
            'isim':request.user.get_full_name,
        }
    else:
        context = {
            'isim': 'Misafir',
        }
    return render(request, 'home.html',{"context":context,"posts":posts_list})