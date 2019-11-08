from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import Http404
from django.forms import modelformset_factory

import importlib

from . import models
from . import forms


#######################################################################################################################
# Form-based interface: server-side only
#######################################################################################################################

def room_view(request):
    RoomFormset = modelformset_factory(models.Room, form=forms.RoomForm, can_delete=True)

    if request.method == 'POST':
        formset = RoomFormset(request.POST)
        if formset.is_valid():
            formset.save()
    else:
        if request.user.is_authenticated:
            rooms = models.Room.objects.filter(owner=request.user)
            formset = RoomFormset(queryset=rooms)
        else:
            formset = []

    #print(formset)
    return render(request, 'rooms.html', {'formset': formset})

def node_form(request):
    # NodeFormset=modelformset_factory(models.Node, form=forms.NodeForm)
    NodeFormset = modelformset_factory(models.Node, form=forms.NodeForm, can_delete=True)

    if request.method == 'POST':
        formset = NodeFormset(request.POST)
        if formset.is_valid():
            formset.save()
    else:
        if request.user.is_authenticated:
            rooms = list(models.Room.objects.filter(owner=request.user))
            nodes = models.Node.objects.filter(location__in=rooms)
            formset = NodeFormset(queryset=nodes)
        else:
            formset = []
    return render(request, 'nodes.html', {'formset': formset, "capabilities": models.capabilities
        if request.user.is_authenticated else []})


def capability_form(request, node_id, capability):
    # get model class
    if capability in models.capabilities:
        cap = models.capabilities[capability]
        # print(cap["name"])
        model = getattr(importlib.import_module("RaspNodeConfig.models"), cap["model"])
        form = getattr(importlib.import_module("RaspNodeConfig.forms"), cap["form"])
    else:
        raise Http404('Capability not found')
    CapabilityFormset = modelformset_factory(model, form=form, can_delete=True)
    if request.method == 'POST':
        formset = CapabilityFormset(request.POST, queryset=model.objects.filter(node__exact=node_id))
        if formset.is_valid():
            formset.save()
    else:
        # formset = CapabilityFormset(queryset=model.objects.filter(node__id__exact=node_id))
        formset = CapabilityFormset(queryset=model.objects.filter(node__exact=node_id))
    node = models.Node.objects.filter(id=node_id)[0]
    room = node.location
    return render(request, 'capabilities.html', {'formset': formset, 'room': room})


