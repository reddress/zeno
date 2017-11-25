from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Post

class IndexView(generic.ListView):
    template_name = "bulletinboard/index.html"
    context_object_name = "latest_posts"

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Post

# Cannot use with @login_required
# class AddView(generic.DetailView):
    # model = Post
    # template_name = "bulletinboard/add.html"

@login_required
def add_form(request):
    return render(request, 'bulletinboard/add.html')
    
@login_required
def add(request):
    try:
        title = request.POST['title']
        body = request.POST['body']
    except KeyError:
        return render(request, 'bulletinboard/add.html',
                      {'error_message': "Could not read title or body"})
    else:
        new_post = Post(author=request.user, title=title, body=body)
        new_post.save()
        return HttpResponseRedirect(reverse('bulletinboard:index'))
