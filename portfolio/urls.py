from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects_list, name='projects'),
    path('books/', views.books_list, name='books'),
    path('papers/', views.papers_list, name='papers'),
    path('blog/', views.blog_list, name='blog'),
    path('appointments/', views.appointments, name='appointments'),
    path('appointment-submit/', views.appointment_submit, name='appointment_submit'),
    path('contact/', views.contact_submit, name='contact_submit'),
]