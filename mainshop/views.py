from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import Products, Category, Cart, Comment
from django.http import Http404, JsonResponse
import json
from .forms import CommentForm
from django.db.models import Q


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



def post_detail(request, pk):
    product = Products.objects.filter(pk = pk).first()
    context = {}
    context['product'] = product

    cm = Comment.objects.filter(product_id=pk, is_publish=True)

    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.user = request.user
            form.product = product
            form.save()
            context['form'] = form
            return redirect('detail', pk)
    else:
        form = CommentForm()
        context['form'] = form

    context['cm'] = cm

    return render(request, 'mainshop/detail.html', context)


def add_to_cart(request, pk):
    current_user = request.user
    cart_item = Cart.objects.filter(user=current_user, product=pk)
    if cart_item:
        for i in cart_item:
            i.quantity += 1
            i.save()
            messages.success(request, "Item added to your cart.")
    else:
        Cart.objects.create(user=current_user, product_id=pk, quantity = 1)
        messages.success(request, "Item added to your cart.")

    return redirect("/product/")



def checkout(request):
    context = {}
    cart_items = Cart.objects.filter(user=request.user)
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

    cart_item = Cart.objects.filter(user=request.user,product_id=prod_id)[0]

    if cart_item:
        if action == 'add':
            cart_item.quantity += 1
        elif action == 'remove':
            cart_item.quantity -= 1
        cart_item.save()

        if cart_item.quantity == 0:
            cart_item.delete()


    return JsonResponse({'status':'Update successfully!'})


class SearchView(ListView):
    model = Products
    template_name = 'mainshop/search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):

        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Products.objects.filter(Q(title__contains=query) | Q(description__icontains=query))
            result = postresult
        else:
            result = None
        return result