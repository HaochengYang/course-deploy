from django.shortcuts import render, redirect
from .models import User
from ..course.models import Course
from django.core.urlresolvers import reverse
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'logreg/index.html')

def register(request):
    response = User.objects.add_user(request.POST)
    if response['status']:
        # successful add a new user in here
       request.session['user_id'] = response['new_user'].id
       request.session['user_first_name'] = response['new_user'].first_name
       request.session['user_last_name'] = response['new_user'].last_name
       return redirect('logreg:main')
    else:
       for error in response['errors']:
           messages.error(request, error)
    return redirect('logreg:index')

def login(request):
    response = User.objects.check_user(request.POST)
    if response['status']:
        # successful login user in here
       request.session['user_id'] = response['login_user'].id
       request.session['user_first_name'] = response['login_user'].first_name
       request.session['user_last_name'] = response['login_user'].last_name
       return redirect('logreg:main')
    else:
       #falid to validate
       for error in response['errors']:
           messages.error(request, error)
       return redirect('logreg:index')

def main(request):
    if "user_id" not in request.session:
        messages.error(request,"Must be Loggin in")
        return redirect('logreg:index')
    else:
        return redirect(reverse('course:index'))

def logout(request):
    request.session.clear()
    return redirect('logreg:index')
