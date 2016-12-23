from django.shortcuts import render
from lab.models import Car, Address, Sales, RegistrationForm, AuthorizationForm
from lab.models import User1
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# def base(request):
#     return render(request, 'lab/base.html', {})

def main(request):
    return render(request, 'lab/main.html', {})


class CarView(View):
    def get(self, request):
        model_row = Car.objects.all()
        page = request.GET.get('page')
        paginator = Paginator(model_row, 1)
        try:
            model_row = paginator.page(page)
        except PageNotAnInteger:
            model_row = paginator.page(1)
        except EmptyPage:
            model_row = paginator.page(paginator.num_pages)
        return render(request, 'lab/model_row.html', {'model_row': model_row})


class AddressView(View):
    def get(self, request):
        address = Address.objects.all()
        return render(request, 'lab/address.html', {'address': address})


class SalesView(View):
    def get(self, request):
        sales = Sales.objects.all()
        return render(request, 'lab/sales.html', {'sales': sales})


class UserView(View):
    def get(self, request):
        users = User1.objects.all()
        return render(request, 'lab/users.html', {'users': users})


def error_auth(request):
    return render(request, 'lab/logout.html')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
            return HttpResponseRedirect('/success/')
    else:
        form = RegistrationForm()
    return render(request, 'lab/registration.html', {'form': form})


@login_required(login_url='/error/')
def login_success(request):
    # if not request.user.is_authenticated():
        # return HttpResponseRedirect('/')
    return render(request, 'lab/login.html')


def authorization(request):
    if request.method == 'POST':
        form = AuthorizationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data.get('username'), password=data.get('password'))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/success/')
    else:
        form = AuthorizationForm()
    return render(request, 'lab/authorization.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/error/')

