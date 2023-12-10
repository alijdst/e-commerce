from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as password_views

from azbankgateways.urls import az_bank_gateways_urls
from mainshop.bank import go_to_gateway_view, callback_gateway_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('mainshop.urls')),
    path('account/', include('account.urls')),

    # bankgetways urls
    path('bankgateways/', az_bank_gateways_urls()),
    path('go-to-gateway/', go_to_gateway_view, name='go-to-gateway'),
    path('callback-gateway/', callback_gateway_view, name='callback-gateway'),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', password_views.PasswordChangeDoneView.as_view(template_name='password_change/password_change_done.html'),
        name='password_change_done'),

    path('password_change/', password_views.PasswordChangeView.as_view(template_name='password_change/password_change.html'),
        name='password_change'),

    path('password_reset/done/', password_views.PasswordResetCompleteView.as_view(template_name='password_change/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', password_views.PasswordResetConfirmView.as_view(template_name='password_change/password_reset_confirm.html'), name='password_reset_confirm'),

    path('password_reset/', password_views.PasswordResetView.as_view(template_name='password_change/password_reset_form.html'), name='password_reset'),

    path('reset/done/', password_views.PasswordResetCompleteView.as_view(template_name='password_change/password_reset_complete.html'),
     name='password_reset_complete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)