from django.shortcuts import render
from .models import Reading
# Create your views here.

def index(request):
    latest_readings = Reading.objects.order_by('-reading_timestamp')[:20]
    return render(request, 'dashboard/dashboard.html', {'latest_readings': latest_readings})
