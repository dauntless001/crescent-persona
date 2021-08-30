from django.urls import path
from personality import views as PersonalityViews 

app_name = 'personality'

urlpatterns = [
	path('', PersonalityViews.personality_answers, name='personality_answers'),
	path('pdf/', PersonalityViews.personalty_from_pdf, name='pdf'),
]