from django.contrib import messages
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import Products, Category, Cart
from django.http import Http404, request, JsonResponse
import json
from django.urls import reverse, reverse_lazy


class HomePage(TemplateView):
    template_name = 'index.html'


class AboutPage(TemplateView):
    template_name = 'mainshop/about.html'


class ProductView(ListView):
    template_name = 'index.html'
    model = Products
    context_object_name = 'product'

class CategoryView(ListView):

    template_name = 'mainshop/category.html'
    model = Products
    context_object_name = 'product'

    # def post_category(request, cat):
    #     cat = cat.replace("-", " ")
    #     category = Category.objects.get(catt=cat)
    #     products = Products.objects.filter(cat=category)
    #     return render(request, 'mainshop/category.html', {'product':products, 'category':category})


    def get_queryset(self):
        category = Category.objects.get(catt=self.kwargs['cat'])
        my_object = Products.objects.filter(cat=category)

        try:
            if my_object.exists():
                return my_object
            else:
                raise Http404("This product does not exists")
        except:
            return redirect("home")

    def get_context_data(self, **kwargs):

        # category = Category.objects.get(catt=self.kwargs['cat'])
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(catt=self.kwargs['cat'])
        context['all_category'] = Category.objects.all()

        return context



class ProductDetailView(DetailView):
    template_name = 'mainshop/detail.html'
    model = Products
    context_object_name = 'product'

    def post_detail(request, pk):
        product = get_object_or_404(Products, pk = pk)
        context = {
            'product': product
        }
        return render(request, 'mainshop/home.html', context)


# class ShopCartView(DetailView):
#     template_name = 'cart/shopcart.html'
#     model = Products
#     context_object_name = 'product'

def add_to_cart(request, pk):
    # if request.method == "POST":
    #     if request.user.is_authenticated:
            cart_item = Cart.objects.filter(product=pk).first()
            if cart_item:
                cart_item.quantity += 1
                cart_item.save()
                messages.success(request, "Item added to your cart.")
            else:
                Cart.objects.create(product_id=pk, quantity = 1)
                messages.success(request, "Item added to your cart.")

            return redirect("/product/")

            # product_id = int(request.POST.get('product_id'))
            # print("product_ID", product_id)
            # product_check = Products.objects.get(id=product_id)
            # if product_check:
            #     if Cart.objects.filter(product_id=product_id):
            #         return JsonResponse({'status': 'Already in cart!!'})
            #     else:
            #         product_qyt = 1
            #         Cart.objects.create(product_id = product_id, quantity = product_qyt)
            #         return JsonResponse({'status': 'Added successfully to cart!'})
            # else:
            #     return JsonResponse({'status': 'Not Found!!'})

    #     else:
    #         return JsonResponse({'status':'Login!!'})
    #
    # return redirect('/')


def checkout(request):
    context = {}
    cart_items = Cart.objects.all()
    context['cart_items'] = cart_items
    context['cart_total'] = cart_items.count()

    cart_total = 0
    total_price = 0
    if cart_items:
        for item in cart_items:

            cart_total += item.quantity
            if item.product.is_sale:
                total_price += item.product.sale_price * item.quantity
            else:
                total_price += item.product.price * item.quantity

        context['total_price'] = total_price
        context['cart_total'] = cart_total

    return render(request, 'mainshop/checkout.html', context)


def update_cart(request):
    data = json.loads(request.body)
    prod_id = data['productId']
    action = data['action']

    cart_item = Cart.objects.filter(product_id=prod_id)[0]

    if cart_item:
        if action == 'add':
            cart_item.quantity += 1
        elif action == 'remove':
            cart_item.quantity -= 1
        cart_item.save()

        if cart_item.quantity == 0:
            cart_item.delete()


    return JsonResponse({'status':'Update successfully!'})