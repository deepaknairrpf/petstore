from rest_framework import serializers
from pets.models import Pet, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')


class PetSerializer(serializers.ModelSerializer):
    owner_username = serializers.PrimaryKeyRelatedField(source='owner', queryset=User.objects.all())

    class Meta:
        model = Pet
        fields = "__all__"


