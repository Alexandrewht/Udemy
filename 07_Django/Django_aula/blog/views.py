from django.shortcuts import render
from .data import posts

def blog(request):
    print('blog')
    
    context = {
            'text': 'Olá Blog!',
            'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context
    )

def exemplo(request):
    print('exemplo')
    context = {
            'text': 'Olá Exemplo!'
    }

    return render(
        request,
        'blog/exemplo.html',
        context
    )
