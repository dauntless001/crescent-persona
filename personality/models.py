from django.db import models

# Create your models here.

class Persona(models.Model):
	name = models.CharField(max_length=255, unique=True)
	description = models.TextField()

	class Meta:
		verbose_name = 'Persona'
		verbose_name_plural = 'Personas'


	def __str__(self):
		return self.name

class PersonaTrait(models.Model):
	persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
	name = models.CharField(max_length=40)
	created_at = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name = 'Persona Trait'
		verbose_name_plural = 'Persona Traits'
		ordering = ['-created_at']


	def __str__(self):
		return self.name



