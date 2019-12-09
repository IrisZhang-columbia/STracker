import IPython
from django.http import HttpResponseNotAllowed, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404

# Create your views here.
from tracker.forms import SightingForm
from tracker.models import Sighting


def add(request):
    if request.method == 'GET':
        form = SightingForm()
        return render(request, 'tracker/add.html', {'form': form})
    elif request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return HttpResponseRedirect('/sightings/{}/'.format(instance.unique_squirrel_id))
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


def map(request):
    if request.method == 'GET':
        return render(request, 'tracker/map.html', {'sightings': Sighting.objects.order_by('?')[:100]})
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


def sighting(request, unique_squirrel_id):
    if request.method == 'GET':
        sighting = get_object_or_404(Sighting, pk=unique_squirrel_id)
        form = SightingForm(instance=sighting)
        return render(request, 'tracker/sighting.html', {'form': form})
    elif request.method == 'POST':
        sighting = get_object_or_404(Sighting, pk=unique_squirrel_id)
        form = SightingForm(request.POST, instance=sighting)
        if form.is_valid():
            return render(request, 'tracker/sighting.html', {'form': form})
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


def sightings(request):
    if request.method == 'GET':
        return render(request, 'tracker/sightings.html', {'sightings': Sighting.objects.all()})
    else:
        return HttpResponseNotAllowed(['GET'])

def stats(request):
    if request.method == 'GET':
        return render(request, 'tracker/stats.html')
    else:
        return HttpResponseNotAllowed(['GET'])
