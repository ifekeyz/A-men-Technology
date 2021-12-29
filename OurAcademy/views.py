from django.shortcuts import render
from .models import Academy
# Create your views here.
def academy(request):
    academic = Academy.objects.order_by('-Academy_date')


    context={
        'academic': academic
    }
    return render(request, 'Pages/academy.html', context)