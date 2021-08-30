from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
import random
from PyPDF2 import PdfFileReader
from personality.forms import CVForm 
from personality.models import PersonaTrait, Persona
from collections import Counter
# Create your views here.

personality = {
	0 : 'Agreeebleness',
	1 : 'Conscientiousness',
	2 : 'Extroversion',
	3 : 'Neuroticism',
	4 : 'Openness',
}


def personalty_from_pdf(request):
	name = ''
	cv = ''
	personalities = [a.name for a in PersonaTrait.objects.all()]
	if request.method == 'POST':
		cv = CVForm(request.POST, request.FILES)
		if cv.is_valid():
			name = cv.cleaned_data['name']
			cv = cv.cleaned_data['cv']
			pdf = PdfFileReader(cv)
			page = pdf.getPage(0)
			page_content = page.extractText()
			print(page_content.encode('utf-8'), 'pages')
	context = {
	'name':name,
	'personality':Persona.objects.get(id=random.randint(1, Persona.objects.count())),
	'bgColor':f'rgba({random.randint(0, 100)}, {random.randint(0, 100)}, {random.randint(0, 100)}, 0.1)'
	}
	return render(request,'personality.html' ,context)





def personality_answers(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		traits = request.POST.getlist('traits')
		categories = [int(a.split('$')[0]) for a in traits]
		personality_ids = [p.id for p in Persona.objects.all()]
		max_cat = 1
		for a in personality_ids:
			if categories.count(a) >= max_cat:
				max_cat = a
		# a, b, c, d, e = categories.count(), categories.count(1), categories.count(2), categories.count(3), categories.count(4)
		# print(a, b, c, d)
		# if (a >= b) and (a >= c) and (a >= d) and (a >=e):
		# 	persona = 0
		# elif (b >= a)  and (b >= c) and (b >= d):
		# 	persona = 1
		# elif (c >= a) and (c >= b) and (c >= d):
		# 	persona = 2
		# else:
		# 	persona = 3
		# traits_list = [a.split('$')[1] for a in traits]
		context = {
		'name' : name,
		'personality' : Persona.objects.get(id=max_cat),
		'bgColor' : f'rgba({random.randint(0, 100)}, {random.randint(0, 100)}, {random.randint(0, 100)}, 0.1)'
		}
		template = 'personality.html'
	return render(request, template, context)

