from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    books= Book.objects.all()
    data_box = {"books": books}
    return render(request,'index.html',context=data_box)
    