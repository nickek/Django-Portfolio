from django.shortcuts import redirect
from django.template import loader
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse, response
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home_view(request):
    group = None
    group_status = False
    if request.user.groups.exists():
        group = request.user.groups.all()[0].name
    if group == 'elevated':
        group_status = True
    template = loader.get_template('home/home.html')
    return HttpResponse(template.render({'group_status': group_status}, request))


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect.')
    temp = {}
    template = loader.get_template('home/login.html')
    return HttpResponse(template.render(temp, request))


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('login')
    else:
        form = CreateUserForm()
    template = loader.get_template('home/register.html')
    return HttpResponse(template.render({'form': form}, request))


def logout_view(request):
    logout(request)
    return redirect('login')
# Create your views here.
