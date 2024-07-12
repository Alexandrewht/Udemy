from django.shortcuts import render


def home(request):
    print('home')

    return render(
        request,
        'global/base.html'
    )