from django.contrib.auth.views import LoginView, LogoutView
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from auth_app.forms import ShopUserLoginForm, ShopUserProfileEditForm, ShopUserCreationForm, ShopUserEditForm


class SignUpView(CreateView):
    template_name = 'auth_app/signup.html'
    form_class = ShopUserCreationForm
    success_url = reverse_lazy('auth_app:signin')


class SignInView(LoginView):
    authentication_form = ShopUserLoginForm
    template_name = 'auth_app/signin.html'


class SignOutView(LogoutView):
    next_page = 'main_app:index'


@transaction.atomic
def edit(request):
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, instance=request.user)
        profile_form = ShopUserProfileEditForm(request.POST, request.FILES, instance=request.user.shopuserprofile)

        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth_app:edit'))

    else:
        edit_form = ShopUserEditForm(instance=request.user)
        profile_form = ShopUserProfileEditForm(instance=request.user.shopuserprofile)

    context = {
        'edit_form': edit_form,
        'profile_form': profile_form
    }
    return render(request, 'auth_app/edit.html', context)




