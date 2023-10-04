import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _


@login_required(login_url='login')
def dashboard(request):
    context = {}
    return render(request, 'be/pages/dashboard.html', context)


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, _('You are logged out successfully!'))
    return redirect('home')