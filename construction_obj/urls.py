from django.urls import path

from construction_obj.views import ListBuildingView, DetailBuildingView, UpdateSectionView

app_name = "construction_obj"

urlpatterns = [
    path("", ListBuildingView.as_view(), name="list_buildings"),
    path("building/<int:pk>/", DetailBuildingView.as_view(), name="detail_building"),
    path("update_section/<int:pk>/", UpdateSectionView.as_view(), name="update_section"),

]
