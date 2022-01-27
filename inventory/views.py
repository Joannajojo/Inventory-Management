from django.shortcuts import render
from inventory.models import Inventory
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views import generic
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
    
    def get(self, request):
        
        name = request.GET.get('name')
        if name:
            item = Inventory.objects.get(name=name)
            serializer = InventorySerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        items = Inventory.objects.all()
        serializer = InventorySerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)        
        