from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index, name="index"),
    url(r'^course$',views.course, name="course"),
    url(r'^location$',views.location, name="location"),
    url(r'^connect$',views.connect, name="connect"),
    url(r'^destroy_course/(?P<id>\d+)$',views.destroy_course, name="destroy_course"),
    url(r'^destroy_location/(?P<id>\d+)$',views.destroy_location, name="destroy_location"),
    url(r'^destroy_database$',views.destroy_database, name="destroy_database")
]
