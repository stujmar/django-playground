from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'auther': 'Stuart Marsh',
        'title': 'blog post one',
        'content': 'First post content',
        'date_posted': 'Auguest 23, 2018'
    },
    {
        'auther': 'Ally Brisbin',
        'title': 'blog post two',
        'content': 'Second post content',
        'date_posted': 'Auguest 23, 2018'
    },
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')