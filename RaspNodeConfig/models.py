from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=40)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Node(models.Model):
    name = models.CharField(max_length=40)
    location = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.name)

capabilities={
    "tapparelle":{
        "name":"tapparelle",
        "model": "TapparelleCapabilityEntry",
        "form": "TapparelleCapabilityForm",
        "serializer": "TapparelleCapabilitySerializer",
    },
    "temperatura":{
        "name":"temperatura",
        "model": "TemperaturaCapabilityEntry",
        "form": "TemperaturaCapabilityForm",
        "serializer": "TemperaturaCapabilitySerializer",
    },
    "switch": {
        "name": "switch",
        "model": "SwitchCapabilityEntry",
        "form": "SwitchCapabilityForm",
        "serializer": "SwitchCapabilitySerializer",
    },
    "button": {
        "name": "button",
        "model": "ButtonCapabilityEntry",
        "form": "ButtonCapabilityForm",
        "serializer": "ButtonCapabilitySerializer",
    }
}


class GenericCapabilityEntry(models.Model):
    name = models.CharField(max_length=40)
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    capability = "generic"

    def get_topic(self):
        return "home/" + self.node.name + "/" + self.capability + "/" + self.name


class TapparelleCapabilityEntry(GenericCapabilityEntry):
    capability = "tapparelle"
    descrizione = models.CharField(max_length=255)
    timeout = models.IntegerField()
    pinUp = models.CharField(max_length=10)
    pinDown = models.CharField(max_length=10)


class TemperaturaCapabilityEntry(GenericCapabilityEntry):
    capability = "temperatura"
    descrizione = models.CharField(max_length=255)
    update = models.IntegerField()
    pin = models.CharField(max_length=10)
    sensor = models.CharField(max_length=10)


class SwitchCapabilityEntry(GenericCapabilityEntry):
    capability = "switch"
    descrizione = models.CharField(max_length=255)
    # Longer pin field because we can have multiple pins for a single switch
    pin = models.CharField(max_length=255)

    def __str__(self):
        return str(self.descrizione)


class ButtonCapabilityEntry(GenericCapabilityEntry):
    capability = "button"
    descrizione = models.CharField(max_length=255)
    pin = models.CharField(max_length=10)
    # Multiple topic can be supported
    topic = models.ForeignKey(SwitchCapabilityEntry, on_delete=models.CASCADE)
