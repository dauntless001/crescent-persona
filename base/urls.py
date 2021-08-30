from django.urls import path
from base import views as BaseViews 

app_name = 'base'

urlpatterns = [
	path('', BaseViews.IndexView.as_view()),
]