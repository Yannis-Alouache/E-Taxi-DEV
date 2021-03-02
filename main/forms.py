from django import forms
from .models import Reservation
from django.forms import ModelForm
from datetime import datetime
import re

class loginForm(forms.Form):
    password = forms.CharField(max_length=22)

    def clean(self):
        data = super().clean()

        password = data.get("password")

        if password:
            if password != "<<Pppp<<1":
                raise forms.ValidationError("Le mot de passe n'est pas le bon")
        

class reservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'phone', 'date', 'addressDeparture', 'addressArrival']

    def clean(self):
        data = super().clean()
        
        phone = data.get('phone')
        dateEntered = data.get('date')
        addressDeparture = data.get('addressDeparture')
        addressArrival = data.get('addressArrival')

        nowUnformatted = datetime.now()
        now = nowUnformatted.strftime("%d/%m/%Y %H:%M")
    
        phonePattern = re.compile(r"^(?:(?:\+|00)33[\s.-]{0,3}(?:\(0\)[\s.-]{0,3})?|0)[1-9](?:(?:[\s.-]?\d{2}){4}|\d{2}(?:[\s.-]?\d{3}){2})$")
        datePattern = re.compile(r"^([0]?[1-9]|[1|2][0-9]|[3][0|1])[./-]([0]?[1-9]|[1][0-2])[./-]([0-9]{4}) ([0-9]{2}):([0-9]{2})$")

        city_autorized = [
        "Lille",
        "Marcq-en-Barœul",
        "Mons-en-Barœul",
        "Marquette-lez-Lille",
        "Villeneuve-d'Ascq", 
        "Lambersart", 
        "Saint-André-lez-Lille",
        "Sequedin",
        "Verlinghem",
        "Pérenchies",
        "Loos",
        "Wambrechies",
        "Roubaix",
        "Armentières",
        "Seclin",
        "Tourcoing",
        "Hellemmes",
        "Haubourdin",
        "Roncq",
        "Capinghem",
        "Lomme",
        "Englos",
        "Lesquin",
        "Faches-Thumesnil",
        "Ronchin",
        "Wazemmes",
        "Lezennes",
        "Wasquehal",
        "Wattignies"
        ]

        city_autorized_check = []

        if dateEntered:
            if re.match(datePattern, dateEntered):  
                dayDateEntered = dateEntered[0] + dateEntered[1]
                dayDateEntered = int(dayDateEntered)

                monthDateEntered = dateEntered[3] + dateEntered[4]
                monthDateEntered = int(monthDateEntered)

                yearDateEntered = dateEntered[6] + dateEntered[7] + dateEntered[8] + dateEntered[9]
                yearDateEntered = int(yearDateEntered)

                hourDateEntered = dateEntered[11] + dateEntered[12]
                hourDateEntered = int(hourDateEntered)

                minuteDateEntered = dateEntered[14] + dateEntered[15]
                minuteDateEntered = int(minuteDateEntered)



                dayNow = now[0] + now[1]
                dayNow = int(dayNow)

                monthNow = now[3] + now[4]
                monthNow = int(monthNow)

                yearNow = now[6] + now[7] + now[8] + now[9]
                yearNow = int(yearNow)

                hourNow = now[11] + now[12]
                hourNow = int(hourNow)

                minuteNow = now[14] + now[15]
                minuteNow = int(minuteNow)

                dateIsValid = None
                dayIsPassed = None
                hourIsPassed = None

                if dayDateEntered > dayNow or monthDateEntered > monthNow:
                    dayIsPassed = True

                if hourDateEntered > hourNow or dayIsPassed == True:
                    hourIsPassed = True
        
                if yearDateEntered > yearNow or yearDateEntered == yearNow:
                    if monthDateEntered > monthNow or monthDateEntered == monthNow:
                        if dayDateEntered > dayNow or dayDateEntered == dayNow or monthDateEntered > monthNow:
                            if hourDateEntered > hourNow or hourDateEntered == hourNow or dayIsPassed == True:
                                if minuteDateEntered > minuteNow or minuteDateEntered == minuteNow or hourIsPassed == True:
                                    print("Tout va bien")
                                    dateIsValid = True
                                else:
                                    print("minute est dépassé")
                            else:
                                print("\nheure est dépassé\n")
                        else:
                            print("jour est dépassé")
                    else:
                        print("mois est dépassé")
                else:
                    print("année est dépassé")


        for city in city_autorized:
            if city not in addressDeparture:
                city_autorized_check.append(False)
            else:
                city_autorized_check.append(True)


        # PHONE VERIFICATION
        if phone:
            if not re.match(phonePattern, phone):
                raise forms.ValidationError('Entrez un numéro de téléphone valide')

        # DATE VERIFICATION
        if dateEntered:
            if not re.match(datePattern, dateEntered):
                raise forms.ValidationError('Entrez une date valide')

            print("Date entered : ", dateEntered)
            print("Today : ", now)

            if dateIsValid != True:
                raise forms.ValidationError('Cette date est deja passé')
        
        # ADDRESS VERIFICATION
        if addressDeparture == addressArrival:
            raise forms.ValidationError("L'adresse de départ et l'adresse d'arrivé ne peuvent être les même")

        if addressDeparture:
            if True not in city_autorized_check:
                raise forms.ValidationError('Vous pouvez seulement partire de Lille et ses environs')
        
