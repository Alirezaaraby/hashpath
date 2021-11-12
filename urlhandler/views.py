from django.http import HttpResponse
from .models import Data


def my_view(request):
    start = request.GET['start']
    end = request.GET['end']
    Data.objects.create(start = start, end= end)
    return HttpResponse(Data.objects.all())
