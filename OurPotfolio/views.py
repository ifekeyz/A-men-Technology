from django.shortcuts import render
from .models import Project
# Create your views here.
def potfolio(request):
    projects = Project.objects.order_by('-Project_date')


    context={
        'projects': projects
    }
    return render(request, 'Pages/potfolio.html', context)