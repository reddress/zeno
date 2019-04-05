from django.shortcuts import render, redirect

from .models import DictEntry

def index(request):
    return render(request, "forlang/greek.html")

def addEntry(request):
    if request.method == "POST":
        english = request.POST.get("english")
        foreign = request.POST.get("foreign")
        example = request.POST.get("example")
        redir = request.POST.get("redir")
        
        DictEntry.objects.create(english=english, foreign=foreign, example=example)
        return redirect(redir)
        
    else:
        return render(request, 'forlang/index.html')
