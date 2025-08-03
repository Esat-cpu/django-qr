from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from olustur.models import URLs


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Hesabınız başarıyla oluşturuldu! Artık giriş yapabilirsiniz.")
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
def profile_update(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, "Hesabınız başarıyla güncellendi!")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/user_update.html', context)


@login_required
def url_delete(request, pk):
    url = get_object_or_404(URLs, pk=pk, author=request.user)
    
    if request.method == "POST":
        url.delete()

    return redirect("profile")
