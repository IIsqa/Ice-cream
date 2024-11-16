
from django.urls import path
from accounts.views import *#-
from accounts.views import login_view, register_view#+

urlpatterns = [
    path('login/', login_view ,name='login_page'), # type: ignore#-
    path('login/', login_view, name='login_page'),#+
    path('register/', register_view, name='register_page'),
]

