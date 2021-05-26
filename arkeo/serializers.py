from rest_framework import serializers
from arkeo.models import MeteoStation, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class MeteoStationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = MeteoStation
        fields = ['id', 'name', 'code', 'linenos', 'language', 'style', 'owner']
        # fields = "__all__"

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
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    stations = serializers.PrimaryKeyRelatedField(many=True, queryset=MeteoStation.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'stations']
