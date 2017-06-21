from django.shortcuts import render
from datetime import datetime, date, time
from .forms import NewclientsForm

def news(request):

    name = "Ildar"
    date = datetime.today()
    form = NewclientsForm(request.POST or None)
    return render(request, 'news/news.html', locals())