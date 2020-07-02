from django.shortcuts import render
from .models import Blog

def home(request):
    blogs = Blog.objects #models.py로 부터 객체모델을 전달받음 = 쿼리셋 (메소드)
    return render(request, 'home.html', {'blogs': blogs})