from django.http import JsonResponse
from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import SubwayMapSerializer
from .models import SubwayMap


class SubwayAPI(APIView):
    def get(request, *args, **kwargs):
        qs = SubwayMap.objects.all()
        serializer = SubwayMapSerializer(qs, many=True)
        return Response(serializer.data)



    def post(self, request, *args, **kwargs):
        serializer = SubwayMapSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)