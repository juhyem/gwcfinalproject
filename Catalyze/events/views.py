from django.shortcuts import render
from django.utils import timezone
from .models import Event
from django.shortcuts import render, get_object_or_404
from .forms import EventForm
from django.shortcuts import redirect
#
# Create your views here.

def index(request):
    return render(request, 'events/index.html', {})

def post_list(request):
    posts = Event.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'events/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Event, pk=pk)
    return render(request, 'events/post_detail.html', {'post': post})
#
def post_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = EventForm()
    return render(request, 'events/post_edit.html', {'form': form})
#
def post_edit(request, pk):
    post = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = EventForm(instance=post)
    return render(request, 'events/post_edit.html', {'form': form})
