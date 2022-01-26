from django.shortcuts import render
from inventory.models import Inventory
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views import generic
from django.views import View
from django.http import Http404


from .serializers import InventorySerializer
# Create your views here.
#request->response
# request handler
#action




class InventoryDetail(generic.DetailView):
    model = Inventory
    
        

class InventoryList(generic.ListView):
    model = Inventory

class InventoryView(APIView):
    #def post(self,request):
     #   serializer = InventorySerializer(data=request.data)
     #   if serializer.is_valid():
      #      serializer.save()
      #      return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
      #  else:
       #     return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Inventory.objects.get(id=id)
            serializer = InventorySerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        items = Inventory.objects.all()
        serializer = InventorySerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)        
        