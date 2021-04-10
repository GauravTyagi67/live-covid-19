from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
def home(request):
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":"india"}#Enter any country

    headers = {
        'x-rapidapi-key': "9e9fdc3ae0mshcc5b3431f9d0e84p117467jsn7a6956ad59d1",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    data = response['response']

    d = data[0]

    print(d)

    context = {
        'all':d['cases']['total'],
        'recovered':d['cases']['recovered'],
        'deaths':d['deaths']['total'],
        'new':d['cases']['new'],
        'critical':d['cases']['critical']
    }

    return render(request,"home.html",context)