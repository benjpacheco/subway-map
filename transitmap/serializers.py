from rest_framework import serializers

from .models import SubwayMap



class SubwayMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubwayMap
        fields = (
            'id', 'subwayline', 'stationname', 'route1', 'route2', 'route3', 'route4',
            'route5', 'route6', 'route7', 'route8',
            'route9', 'route10', 'route11', 'entrancetype', 'entry', 'ada', 'freecrossover',
            'entrancelat', 'entrancelong'
        )