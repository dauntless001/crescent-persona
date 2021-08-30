from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import HttpResponse
from personality.models import PersonaTrait
from personality.forms import CVForm
from base.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


class IndexView(View):
	def get(self, request, *args, **kwargs):
		template = 'index.html'
		context = {'traits':PersonaTrait.objects.all(), 'form':CVForm()}
		return render(request, template, context)

	def post(self, request, *args, **kwargs):
		pass



def loginview(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('base:home')
	return render(request, 'login.html', {'form':form})


def logoutview(request):
	logout(request)
	return redirect('base:home')


