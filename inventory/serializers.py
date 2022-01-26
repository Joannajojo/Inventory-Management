#  convert  Model to JSON

from .models import Supplier,Inventory
from rest_framework import serializers

class InventorySerializer(serializers.ModelSerializer):
    #name= serializers.CharField(max_length=80)
    #description = serializers.CharField(max_length=150)
    #note = serializers.CharField(max_length=150)
    #stock = serializers.IntegerField()
    #availability = serializers.BooleanField()
    #supplier = serializers.ForeignKey(Supplier, on_delete=serializers.CASCADE)
    
    class Meta:
        model = Inventory
        fields = ('__all__')

