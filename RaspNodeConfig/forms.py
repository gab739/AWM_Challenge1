from django.forms import ModelForm
from . import models

class RoomForm(ModelForm):
    class Meta:
        model = models.Room
        fields = ['name', 'owner']

class NodeForm(ModelForm):
    class Meta:
        model = models.Node
        fields = ['id', 'name', 'location']


class TapparelleCapabilityForm(ModelForm):
    class Meta:
        model = models.TapparelleCapabilityEntry
        fields = ['id', 'name', 'descrizione', 'node', 'pinUp', 'pinDown', 'timeout']


class TemperaturaCapabilityForm(ModelForm):
    class Meta:
        model = models.TemperaturaCapabilityEntry
        fields = ['id', 'name', 'descrizione', 'node', 'pin', 'sensor', 'update']


class SwitchCapabilityForm(ModelForm):
    class Meta:
        model = models.SwitchCapabilityEntry
        fields = ['id', 'name', 'descrizione', 'node', 'pin']


class ButtonCapabilityForm(ModelForm):
    class Meta:
        model = models.ButtonCapabilityEntry
        fields = ['id', 'name', 'descrizione', 'node', 'pin', 'topic']
