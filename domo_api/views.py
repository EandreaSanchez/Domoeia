from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from domo_api.models import *
from domo_api.serializers import *

class Locations_method(APIView):
    def post(self, request):
        name_location=request.data["name_location"]
        user=request.data["user_id"]
        Locations.objects.create(name_locations=name_location,user_id=user)
        return Response (status=status.HTTP_200_OK)
    def put(self, request,codigo):
        location=Locations.objects.get(id=codigo)
        location.name_locations=request.data["name_location"]
        location.save()
        print('eyyyy')
        return Response (status=status.HTTP_200_OK)

    def get(self, request,codigo):
        locations=Locations.objects.filter(user_id=codigo)
        content={}
        #location_list=[]
        #for i in locations:
        #    location_list.append({"id":i.id,"name_location":i.name_locations})
        location_list=LocationSerializers(locations,many=True).data
        content["locations"]=location_list
        return Response (content, status=status.HTTP_200_OK)
    
    def delete(self,request,codigo):
        location=Locations.objects.get(id=codigo)
        location.delete()
        return Response (status=status.HTTP_200_OK)
    

class Devices_method(APIView):
    def post(self, request):
        name_device=request.data["name_device"]
        location=request.data["location_id"]
        unit=request.data["unit"]
        Devices.objects.create(name_device=name_device,location_id=location,unit=unit)
        return Response (status=status.HTTP_200_OK)
    
    def put(self, request,codigo):
        device=Devices.objects.get(id=codigo)
        device.name_device=request.data["name_device"]
        device.location_id=request.data["location_id"]
        location.save()
        return Response (status=status.HTTP_200_OK)

    def get(self, request,codigo):
        devices=Devices.objects.filter(user_id=codigo)
        content={}
        #location_list=[]
        #for i in locations:
        #    location_list.append({"id":i.id,"name_location":i.name_locations})
        device_list=DeviceSerializers(devices,many=True).data
        content["devices"]=device_list
        return Response (content, status=status.HTTP_200_OK)
    
    def delete(self,request,codigo):
        device=Devices.objects.get(id=codigo)
        device.delete()
        return Response (status=status.HTTP_200_OK)
    
class Dots_method(APIView):
    def post(self, request):
        value=request.data["value"]
        device_id=request.data["device"]
        Dots.objects.create(value=value,device_id=device_id)
        return Response (status=status.HTTP_200_OK)
    
    def get(self, request,codigo):
        dots=Dots.objects.filter(device=codigo)
        content={}
        #location_list=[]
        #for i in locations:
        #    location_list.append({"id":i.id,"name_location":i.name_locations})
        dots_list=DotsSerializers(dots,many=True).data
        content["dots"]=dots_list
        return Response (content, status=status.HTTP_200_OK)
    
    


   
