from django.shortcuts import render
from .models import Comment

def blog(request):
    comentario=Comment.objects.all()
    return render(request,"core/blog.html",{'comentario':comentario})