from django.contrib import admin
from django.urls import path
from home import views

# manually added

admin.site.site_header = "Hammad Admin"
admin.site.site_title = "Hammad Admin Portal"
admin.site.index_title = "Welcome to Hammad Researcher Portal"

urlpatterns = [
    path('',views.index, name='home'),
    # path("contact", views.contact, name='contact'),
    path("abouts", views.abouts, name='abouts'),
    path("services", views.services, name='services'),
    path("contacts", views.contacts, name='contacts'),
]