from io import BytesIO
import base64
from django.shortcuts import render, redirect
from django.contrib import messages

from .utils import Qr
from .forms import UrlForm
from .models import URLs

def home(request):
    context = {}
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data['url']
            if request.user.is_authenticated:
                URLs.objects.create(url=link, author=request.user)
        else:
            messages.error(request, form.errors)
            return redirect("olustur:home")

        img = Qr(url= link)

        buffer = BytesIO()
        img.save(buffer, format= "PNG")

        img64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        context['qrkod'] = img64
        buffer.close()

    return render(request, "olustur/home.html", context)


def custom_404(request, exception):
    return render(request, 'olustur/404.html', status=404)
