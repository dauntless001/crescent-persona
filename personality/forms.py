from django import forms



class CVForm(forms.Form):
	name = forms.CharField(max_length=255, 
		widget=forms.TextInput(attrs={'class':'form-control'}))
	cv = forms.FileField(
		widget=forms.FileInput(attrs={'class':'form-control', 'id':'formFile', 'accept':'.pdf'}))