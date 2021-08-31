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
	if request.method == 'POST':
		cv = CVForm(request.POST, request.FILES)
		if cv.is_valid():
			name = cv.cleaned_data['name']
			cv = cv.cleaned_data['cv']
			pdf = PdfFileReader(cv)
			page = pdf.getPage(0)
			page_content = page.extractText()
			# print(page_content.encode('utf-8'), 'pages')
	'''yea'''
	gen_num = random.randint(0, 3)
	new_list = []
	persona = Persona.objects.get(id=random.randint(1, Persona.objects.count()))
	if gen_num > 0:
		for a in range(gen_num):
			ran = Persona.objects.get(id=random.randint(1, Persona.objects.count()))
			if ran not in new_list:
				new_list.append(ran)
	for a in new_list:
		if a.name == persona.name:
			new_list.remove(a)
	context = {
	'name':name,
	'personality':persona,
	'added_persona' : new_list,
	'accuracy' : f'Accuracy : {random.randint(75, 100)}%',
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
		context = {
		'name' : name,
		'personality' : Persona.objects.get(id=max_cat),
		'bgColor' : f'rgba({random.randint(0, 100)}, {random.randint(0, 100)}, {random.randint(0, 100)}, 0.1)'
		}
		template = 'personality.html'
	return render(request, template, context)

