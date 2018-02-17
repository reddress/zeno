from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views import generic

class IndexView(generic.TemplateView):
    template_name = "users/index.html"

def create_and_login(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'])
            login(request, new_user)
            return HttpResponseRedirect(reverse('users:index'))
    else:
        form = UserCreationForm()
    return render(request, "users/user_creation.html", {"form": form})
    
