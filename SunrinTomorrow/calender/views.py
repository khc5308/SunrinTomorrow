from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView




# from .models import

class EquipmentAPI(APIView):
    def get(self, request, id):
        equipment = get_object_or_404(Equipment, eid=id)
        serializer = EquipmentSerializer(equipment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request, id):
        equipment = get_object_or_404(Equipment, eid=id)
        equipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self, request, id):
        equipment = get_object_or_404(Equipment, eid=id)
        serializer = EquipmentSerializer(equipment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)