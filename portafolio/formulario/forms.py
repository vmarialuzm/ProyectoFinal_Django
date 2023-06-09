from django import forms

class ProyectoForm(forms.Form):
    foto = forms.URLField(widget=forms.TextInput(attrs={
        "class": "form-control mb-3"
    }))
    titulo_proyecto = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        "class": "form-control mb-3"
    })) 
    descripcion_proyecto = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control mb-3"
    }))
    tags = forms.CharField(max_length=200,widget=forms.TextInput(attrs={
        "class": "form-control mb-3"
    }))
    url_github = forms.URLField(widget=forms.TextInput(attrs={
        "class": "form-control mb-3"
    }))