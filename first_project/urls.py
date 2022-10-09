
from django.contrib import admin
from django.urls import path,include
from first_app import views as todolist_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("todolist/",include('first_app.urls')),
    path("account/",include('users_app.urls')),
    path('contact',todolist_views.contact,name='contact'),
    path('about',todolist_views.about,name='about'),
    path('',todolist_views.index,name="index"),
    path('tic',todolist_views.tic,name='tic'),
]
