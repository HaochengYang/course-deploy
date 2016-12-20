from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..logreg.models import User
from django.contrib import messages
from django.db.models import Count
from .models import Course, Location
# Create your views here.
def index(request):
    if "user_id" not in request.session:
        messages.error(request,"Must be Loggin in")
        return redirect('logreg:index')
    else:
        context={
        "Course":Course.objects.all(),
        "Location":Location.objects.all(),
         "User":User.objects.all()
        }
    return render(request,'course/index.html',context)


def course(request):
    if "user_id" not in request.session:
        messages.error(request,"Must be Loggin in")
        return redirect('logreg:index')
    else:
        course = Course.objects.create(title=request.POST['title'],description=request.POST['description'])
        return redirect(reverse('course:index'))

def location(request):
    if "user_id" not in request.session:
        messages.error(request,"Must be Loggin in")
        return redirect('logreg:index')
    else:
        location = Location.objects.create(location=request.POST['location'])
    return redirect(reverse('course:index'))

def destroy_course(request,id):
    if "user_id" not in request.session:
        messages.error(request,"Must be Loggin in")
        return redirect('logreg:index')
    else:
        Course.objects.get(id=id).delete()
    return redirect(reverse('course:index'))

def destroy_location(request,id):
    if "user_id" not in request.session:
        messages.error(request,"Must be Loggin in")
        return redirect('logreg:index')
    else:
        Location.objects.get(id=id).delete()
    return redirect(reverse('course:index'))

def destroy_database(request):
    if "user_id" not in request.session:
        messages.error(request,"Must be Loggin in")
        return redirect('logreg:index')
    else:
        Location.objects.all().delete()
        Course.objects.all().delete()
    return redirect(reverse('course:index'))

def connect(request):
    if "user_id" not in request.session:
        messages.error(request,"Must be Loggin in")
        return redirect('logreg:index')
    else:
        course = Course.objects.get(id=request.POST['course_id'])
        location = Location.objects.get(id=request.POST['location_id'])
        user = User.objects.get(id=request.POST['user_id'])
        course.user.add(user)
        location.course.add(course)
    return redirect(reverse('course:index'))
