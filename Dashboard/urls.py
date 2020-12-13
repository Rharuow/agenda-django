from django.urls import path, include

from . import views

app_name = 'dashboard'

urlpatterns = [
	path('', views.access, name="access"),
	path('home', views.home, name="home"),
	path('users', views.users, name="users"),
	path('account', views.account, name="account"),
	path('registers/1', views.registers_index, name="registers_index"),
	path('registers', views.registers, name="registers"),
	path('registers/top', views.registers_public, name="registers_public"),
	path('registers/create', views.register_create, name="register_create"),
]
