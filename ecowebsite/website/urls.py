from os import name
from . import views
from django.urls import path

app_name = 'website'

urlpatterns = [
    path("", views.home, name = 'home'),
    path("company/", views.about_company, name='about'),
    path("projects/", views.projects, name='projects'),
    path("gallery/", views.gallery, name='gallery'),
    path("people/", views.people, name='people'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('news/', views.news, name='news'),
    path('news/<slug:post>/',views.news_single, name='news_single'),
    path('projects/<slug:tag>/',views.projects, name='projects'),
    path('projects/<slug:tag>/<slug:post>/', views.project_single, name='project_single'), 
    
] 