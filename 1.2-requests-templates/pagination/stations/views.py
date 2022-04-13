import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination.settings import BUS_STATION_CSV

with open(BUS_STATION_CSV, newline='') as csvfile:
    print('Reading data from csv')
    csv_data = csv.DictReader(csvfile)
    DATA = []
    for row in csv_data:
        DATA.append(
            {
                'Name': row['Name'],
                'Street': row['Street'],
                'District': row['District']
            }
        )


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    context = {
        #     'bus_stations': ...,
        #     'page': ...,
    }
    page_num = request.GET.get('page', 1)
    paginator = Paginator(DATA, 10)
    page = paginator.get_page(page_num)
    context = {'bus_stations': page, 'page': page}

    return render(request, 'stations/index.html', context)
