from django.shortcuts import render


def homeView(request):
    context = {}
    return render(request, 'fe/base.html', context)