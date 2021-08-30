from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from personality.models import PersonaTrait
from personality.forms import CVForm
# Create your views here.


class IndexView(View):
	def get(self, request, *args, **kwargs):
		template = 'index.html'
		context = {'traits':PersonaTrait.objects.all(), 'form':CVForm()}
		return render(request, template, context)

	def post(self, request, *args, **kwargs):
		pass
