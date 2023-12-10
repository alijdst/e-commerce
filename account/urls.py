from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
                login_view,
                signup_view,
                logout_view,
                edit_profile_view,
                #profile_view
                    )

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:user_id>/', edit_profile_view, name='profile'),
]