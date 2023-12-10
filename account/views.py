from django.shortcuts import render
from django.http import HttpResponse
from .forms import AccountAuthenticationForm, SignUpForm, EditProfileForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from .models import Account
from django.conf import settings


def login_view(request):
    context = {}
    user = request.user

    if user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            user = authenticate(email=email, password=raw_password, username=username)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'account/login.html', context)


def signup_view(request, *args, **kwargs):
    user = request.user

    if user.is_authenticated:
        return HttpResponse(f"Hi {user.username} you are already signed in")

    context = {}
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email').lower()
            acc = authenticate(email=email, username=username, password = password)
            login(request, acc)
            destination = kwargs.get('next')
            if destination:
                return redirect(destination)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = SignUpForm()
        context['registration_form'] = form
    return render(request, 'account/signup.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

# def profile_view(request, *args, **kwargs):
#     user_id = kwargs.get('user_id')
#     context = {}
#
#     try:
#         account = Account.objects.get(pk=user_id)
#     except:
#         return HttpResponse("something went wrong")
#
#     context['profile'] = account
#
#     return render(request, 'account/profile.html', context)

def edit_profile_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('login')

    user_id = kwargs.get('user_id')

    account = Account.objects.get(pk=user_id)

    dic = {}

    if not account.is_authenticated:
        return redirect('login')

    if account.pk != request.user.pk:
        return HttpResponse("You can not edit this profile!")

    if request.POST:
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile', account.pk)
        else:
            form = EditProfileForm(request.POST, instance=request.user, initial={
                'id': account.id,
                'first_name': account.first_name,
                'last_name': account.last_name,
                'email': account.email,
                'phone_number': account.phone_number,
                'profile_image': account.profile_image,
                'address': account.address
                        }
                                   )
            dic['form'] = form
    else:
        form = EditProfileForm(
            initial={
                'id': account.id,
                'first_name': account.first_name,
                'last_name': account.last_name,
                'email': account.email,
                'phone_number': account.phone_number,
                'profile_image': account.profile_image,
                'address': account.address
            }
        )
        dic['form'] = form
        dic['user'] = account

    dic['DATA_UPLOAD_MAX_MEMORY_SIZE'] = settings.DATA_UPLOAD_MAX_MEMORY_SIZE
    return render(request, 'account/profile.html', dic)

