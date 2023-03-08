from django.shortcuts import render
from .models import Participant
# Create your views here.

def index(request):
    participants = Participant.objects.all()
    rifas_vendidas = 0
    for participant in participants:
        rifas_vendidas += participant.points
    print(rifas_vendidas)
    return render(request, "../templates/rc_house/index.html", {
        'participants': participants,
        'rifas_vendidas': rifas_vendidas
    })