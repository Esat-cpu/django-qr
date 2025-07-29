from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic

from .forms import UserRegisterForm
from .models import URLs


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hesabınız başarıyla oluşturuldu! Artı giriş yapabilirsiniz.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


class ProfileView(LoginRequiredMixin, generic.ListView):
    template_name = 'users/profile.html'
    context_object_name = "urls"

    def get_queryset(self):
        return URLs.objects.filter(author=self.request.user)


@login_required
def url_delete(request, pk):
    url = get_object_or_404(URLs, pk=pk, author=request.user)
    
    if request.method == "POST":
        url.delete()

    return redirect("profile")
