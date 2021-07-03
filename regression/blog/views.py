from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# posts = [
#     {
#         'author': 'Stuart Marsh',
#         'title': 'blog post one',
#         'content': 'First post content',
#         'date_posted': 'August 10, 2020'
#     },
#     {
#         'author': 'Ally Brisbin',
#         'title': 'blog post two',
#         'content': 'Second post content',
#         'date_posted': 'August 24, 2019'
#     },
# ]

# Create your views here.
def home(request):
    context = {
        # 'posts': posts
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})