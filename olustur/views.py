from django.shortcuts import render
from .utils import Qr
from io import BytesIO
import base64

def home(request):
    context = { "titlemz": "QR Kod Oluşturucu" }

    if request.method == "POST":
        link = request.POST.get("link")
        img = Qr(url= link)

        buffer = BytesIO()
        img.save(buffer, format= "PNG")

        img64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        context['qrkod'] = img64
        buffer.close()

    return render(request, "olustur/home.html", context)
