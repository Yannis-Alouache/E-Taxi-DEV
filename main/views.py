from django.shortcuts import render, redirect
from .forms import reservationForm, loginForm
from django.contrib import messages
from .models import Reservation
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
import json
from .models import Reservation
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def home_view(request):
    if request.method == "POST":
        form = reservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre demande de réservation a était envoyée')
            return redirect("home")
        else:
            print("Form is not valid")

    else:
        form = reservationForm()
    
    context = {
        "form":form
    }
    return render(request, "home.html", context)


def login_view(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            user = authenticate(username='mohammed', password='<<Pppp<<1')
            if user is not None:
                login(request, user)
            else:
                print("Existe pas")
            return redirect("race")
        else:
            print("Login Form is not valid")
    else:
        form = loginForm()

    context = {
        "form":form
    }

    return render(request, "login.html", context)


@login_required(login_url="login")
def race_view(request):
    races = Reservation.objects.all()
    context = {
        "races":races
    }
    return render(request, "race.html", context)


def removeRace(request):
    data = json.loads(request.body)

    raceId = data["raceId"]
    raceId = int(raceId)
    Reservation.objects.filter(id=raceId).delete()

    return JsonResponse("Race Supprimé", safe=False)
