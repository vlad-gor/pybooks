from django.shortcuts import render
from .models import Book

all_tags = ['highload', 'devops', 'datascience', 'python', 'инвестиции', 'lego', 'robotics']

# Create your views here.
def index(request):
    '''
    Вывод содержимого основной страницы - добавить фильтрацию по тегам
    Get- запрос - вывод всех книг
    '''
    if request.method == 'POST':
        # здесь будет выбор в соответствии с тегом
        tag_value = request.POST.get("select_tags")
        books= Book.objects.filter(tags__contains=tag_value)
        data_box = {"books": books, "tags":all_tags}
    else:
        books= Book.objects.all()
        data_box = {"books": books, "tags":all_tags}


    return render(request,'index.html',context=data_box)
    