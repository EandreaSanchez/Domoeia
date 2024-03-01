from rest_framework import serializers



class LocationSerializers(serializers.Serializer):
    name_locations =serializers.CharField(max_length=255)
    user_id= serializers.IntegerField()

class DeviceSerializers(serializers.Serializer):
    name_device =serializers.CharField(max_length=255)
    unit=serializers.CharField(max_length=255)
    location_id= serializers.IntegerField()

class DotsSerializers(serializers.Serializer):
    value =serializers.CharField(max_length=255)
    datTime=serializers.CharField(max_length=255)
    device_id= serializers.IntegerField()