from django.urls import path

from . import views as auth_app

app_name = 'auth_app'

urlpatterns = [
    path('signup/', auth_app.SignUpView.as_view(), name='signup'),
    path('signin/', auth_app.SignInView.as_view(), name='signin'),
    path('signout/', auth_app.SignOutView.as_view(), name='signout'),
    path('edit/', auth_app.edit, name='edit'),
]

