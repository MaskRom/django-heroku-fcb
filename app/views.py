from django.shortcuts import redirect, render
#from app.forms import *
from .models import *

#====================利用者ビュー画面====================

def frontpage(request):
    classlist = ClassDB.objects.all()
    return render(request, 'index.html', {'classlist':classlist})

def home(request, fcb_class):
    classlist = ClassDB.objects.all()
    post = ClassDB.objects.get(slug=fcb_class)
    return render(request, 'home.html',{'classlist':classlist, 'post':post,})