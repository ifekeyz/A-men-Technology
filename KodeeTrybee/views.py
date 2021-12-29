from django.shortcuts import render
from .models import KodeeTrybee
# Create your views here.


def kodeeTrybee(request):
    kodeetrybees = KodeeTrybee.objects.order_by('-Push_date')

    context = {
        'kodeetrybees': kodeetrybees
    }
    return render(request, 'Pages/kodeeTrybee.html', context)
