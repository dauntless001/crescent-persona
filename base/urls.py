from django.urls import path
from base import views as BaseViews 

app_name = 'base'

urlpatterns = [
	path('', BaseViews.IndexView.as_view(), name='home'),
	path('login/', BaseViews.loginview, name='login'),
	path('logout/', BaseViews.logoutview, name='logout'),
]