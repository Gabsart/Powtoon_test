from rest_framework import serializers
from .models import Powtoon

# Display all powtoon fields
class PowtoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Powtoon
        fields = '__all__'
        extra_kwargs = {'sharedWith': {'required':False}}


# Display basic powtoon fields
class PowtoonBasicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Powtoon
        # fields = ('id', 'username', 'owner_of')
        fields = ('id', 'name', 'contentJson')

