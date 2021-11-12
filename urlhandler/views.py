from django.http import HttpResponse
from .models import Data


def my_view(request):
    switch = request.GET['switch']
    light = request.GET['light']
    Data.objects.create(switch = switch, light= light)
    return HttpResponse("switch = " + switch +" "+ "light = " + light)
