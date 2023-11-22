from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Producto

def blog(request):
    productos = Producto.objects.all()
    paginator = Paginator(productos, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "core/blog.html", {'productos': page_obj})