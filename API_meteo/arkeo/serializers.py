from rest_framework import serializers
from arkeo.models import MeteoStation, STATION_TYPES
from django.contrib.auth.models import User


class MeteoStationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    lat = serializers.FloatField()
    lon = serializers.FloatField()
    start = serializers.IntegerField()
    st_type = serializers.ChoiceField(choices=STATION_TYPES, default="Not defined")
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = MeteoStation
        fields = ['id', 'name', 'lat', 'lon', 'start', 'st_type']

    def create(self, validated_data):
        """
        Create and return a new `MeteoStation` instance, given the validated data.
        """
        return MeteoStation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `MeteoStation` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.lon = validated_data.get('lon', instance.lon)
        instance.start = validated_data.get('start', instance.start)
        instance.st_type = validated_data.get('st_type', instance.st_type)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    stations = serializers.PrimaryKeyRelatedField(many=True, queryset=MeteoStation.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'stations']
