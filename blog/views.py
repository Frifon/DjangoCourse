# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Material

# Create your views here.


def post_list(request):
    return render(request, 'blog/post_list.html', {'posts': Material.objects.all()})
