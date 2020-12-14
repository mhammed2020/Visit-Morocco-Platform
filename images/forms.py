from django import forms

from .models import Image
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ( 'url','title', 'description')
        widgets = {'url': forms.HiddenInput,}


    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg'] # list requires only two type of images jpg and jpeg
        extension = url.rsplit('.', 1)[1].lower() # split from right the url string and return the extensions
        if extension not in valid_extensions: # make sure that  url is a  jpg or jpeg type 
            raise forms.ValidationError('The given URL does not match valid image extensions.')
        return url

    def save(self, force_insert=False,force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'
        
        response = request.urlopen(image_url)
        image.image.save(image_name,
        ContentFile(response.read()),
        save=False)
        if commit:
            image.save()
        return image