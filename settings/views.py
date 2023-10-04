from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import WebSettings
from .forms import WebSettingsForm


@login_required(login_url='login')
def webSettingsView(request):
    website_settings = WebSettings.objects.first()

    if not website_settings:
        if request.method == 'POST':
            ws_form = WebSettingsForm(request.POST, request.FILES)
            if ws_form.is_valid():
                ws_form.save()
                messages.success(request, 'Your settings have been saved.')
                return redirect('webSettings')
        else:
            ws_form = WebSettingsForm()
    else:
        if request.method == 'POST':
            ws_form = WebSettingsForm(request.POST, request.FILES, instance=website_settings)
            if ws_form.is_valid():
                if ws_form.has_changed():
                    ws_form.save()
                    messages.success(request, 'Your settings have been updated.')
                    return redirect('webSettings')
                else:
                    messages.info(request, 'Nothing has changed.')
            else:
                messages.error(request, 'There was an error with your submission. Please check your data.')
        else:
            ws_form = WebSettingsForm(instance=website_settings)

    context = {
        'website_settings': website_settings,
        'ws_form': ws_form,
    }
    return render(request, 'be/pages/settings/webSettingUpdate.html', context)