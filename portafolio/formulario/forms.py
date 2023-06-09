from django import forms

class ProyectoForm(forms.Form):
    foto = forms.URLField()
    titulo_proyecto = forms.CharField(max_length=200) 
    descripcion_proyecto = forms.CharField(widget=forms.Textarea)
    tags = forms.CharField(max_length=200)
    url_github = forms.URLField()