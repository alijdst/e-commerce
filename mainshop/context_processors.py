from .models import Cart, Category

def cart_counter(request):
    context = {}
    cart_total = 0

    if request.user.is_authenticated:
        cart_item = Cart.objects.filter(user=request.user)

        if cart_item:
            for i in cart_item:
                counter = i.quantity
                cart_total += counter
            context['cart_total'] = cart_total

    return context


def show_category(request):
    context = {}
    active_category = Category.objects.filter(is_active = True)

    context['active_category'] = active_category

    return context

# def search(request):
#     context = {}
#     query = request.GET.get('search')
#     postresult = Products.objects.filter(
#         Q(title__contains=query) | Q(description__icontains=query) | Q(cat__icontains=query))
#
#     context['search'] = postresult
#
#     return context