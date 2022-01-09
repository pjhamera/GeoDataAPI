from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import GeoDataSerializer
from ..models import GeoData 
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend



class UrlDetail(generics.ListAPIView):
    serializer_class = GeoDataSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        url = self.kwargs['url']
        return GeoData.objects.filter(url=url)

class GeoDataList(generics.ListAPIView):
    serializer_class = GeoDataSerializer
    queryset = GeoData.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['continent_code', 'country_name', 'region_name', 'city', 'zip', 'is_eu']

class GeoDataGetAdd(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        geo_data = GeoData.objects.all()
        serializer = GeoDataSerializer(geo_data, many=True, context={'request': request})
        return Response(serializer.data)   

    def post(self, request):
        serializer = GeoDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)   

class IpDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = GeoData.objects.all()
    serializer_class = GeoDataSerializer

class GeoDataCreate(generics.CreateAPIView):
    serializer_class = GeoDataSerializer
    queryset = GeoData.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()    