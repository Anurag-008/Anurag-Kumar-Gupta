from dataclasses import field
from pyexpat import model
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import contact


class contact_serializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        fields = "__all__"
    