#!/usr/bin/env python
from django.db import models


class RaspBerry(models.Model):
    pass


class Arduino(models.Model):
    mac = models.CharField(max_length=17)


class Device(models.Model):
    LIGHT = 'LI'
    TEMPERATURE = 'TE'
    MOVEMENT = 'MO'
    DEVICE_TYPE_CHOICES = (
        (LIGHT, 'Light bulb'),
        (TEMPERATURE, 'Temperature sensor'),
        (MOVEMENT, 'Movement sensor'),
    )
    type = models.CharField(max_length=2, choices=DEVICE_TYPE_CHOICES, default=LIGHT)