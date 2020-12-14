from django.shortcuts import render, redirect
from .forms import ImageCreateForm

def image_create(request):
    if request.method == 'POST': # form saved
    
        form = ImageCreateForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return redirect(new_item.get_absolute_url())

    else:
            
        form = ImageCreateForm(data=request.GET) # show Image form
    return render(request, 'images/image/create.html', {'section': 'images','form': form})