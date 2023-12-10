from django.urls import path, include
from .views import ProductView, CategoryView, HomePage, AboutPage, add_to_cart, checkout, update_cart, post_detail, SearchView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', ProductView.as_view(), name = 'home'),
    path('category/<str:cat>/', CategoryView.as_view(), name = 'category'),
    path('detail/<int:pk>/', post_detail, name = 'detail'),
    path('about/', AboutPage.as_view(), name='about'),
    path('add-to-cart/<int:pk>/', add_to_cart, name='add-to-cart'),
    path('checkout/', checkout, name='checkout'),
    path('update-cart/', update_cart, name='update_cart'),
    path('result/', SearchView.as_view(), name='post_search'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
