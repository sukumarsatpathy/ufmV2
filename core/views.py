from django.shortcuts import render


def homeView(request):
    context = {}
    return render(request, 'fe/pages/home.html', context)