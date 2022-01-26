from django.urls import include,path
from . import views



urlpatterns = [
    path('', views.InventoryList.as_view()),
    path('api/inventory', views.InventoryView.as_view()),
    path('<int:pk>', views.InventoryDetail.as_view())
]