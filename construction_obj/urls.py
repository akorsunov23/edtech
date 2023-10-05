from django.urls import path

from construction_obj.views import ListBuilding, DetailBuilding

app_name = "construction_obj"

urlpatterns = [
    path("", ListBuilding.as_view(), name="list_buildings"),
    path("building/<int:pk>/", DetailBuilding.as_view(), name="detail_building"),
]
