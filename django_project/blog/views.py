from django.shortcuts import render

post = [
    {
        'author': 'JulioAranaJr',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 25, 2024'
    },
    {
        'author': 'Nizar',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 25, 2024'
    }
]

def home(request):
    context = {
        'posts': post
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
