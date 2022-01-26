from django.urls import include,path
from . import views



urlpatterns = [
    path('inventory', views.InventoryList.as_view()),
    path('api/inventory', views.InventoryView.as_view()),
    path('inventory/<int:pk>', views.InventoryDetail.as_view())
]