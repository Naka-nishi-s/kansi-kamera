from django.shortcuts import render
from django.http import HttpResponse
from .models import SampleData

# Create your views here.
def sample_views(request):
    if(request.method == 'POST'):
        response = request.POST['name']
        SampleData.objects.create(content=response)
        return HttpResponse(f'Your Input is {response}, right?')
    else:
        return render(request, 'nice/index.html')