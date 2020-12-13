from django.urls import path, include

from . import views

app_name = 'user'

urlpatterns = [
	path('login/', views.login, name="login"),
	path('sair/', views.logout, name="logout"),
	path('cadastrar/', views.signup, name="signup"),
	path('cadastrar/novo', views.new, name="new"),
]