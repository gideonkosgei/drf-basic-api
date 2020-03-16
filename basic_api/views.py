
from django.shortcuts import render
from rest_framework import generics
from basic_api.models import DRFPost,DRFUser
from basic_api.serializers import DRFPostSerializer, DRFUserSerializer
import logging

logger = logging.getLogger(__name__)


class API_objects(generics.ListCreateAPIView):
    queryset = DRFPost.objects.all()
    serializer_class = DRFPostSerializer
    logger.debug('List all:Information incoming!')     
   

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = DRFPost.objects.all()
    serializer_class = DRFPostSerializer
    logger.info('List One:Information incoming!')  

class API_objects_DRFUser(generics.ListCreateAPIView):
    queryset = DRFUser.objects.all()
    serializer_class = DRFUserSerializer

class API_objects_details_DRFUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = DRFUser.objects.all()
    serializer_class = DRFUserSerializer

    