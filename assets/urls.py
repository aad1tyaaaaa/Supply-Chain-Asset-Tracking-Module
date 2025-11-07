from django.urls import path
from . import views
from .metrics import metrics_view

urlpatterns = [
    # Monitoring
    path('metrics/', metrics_view, name='metrics'),
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Asset URLs
    path('assets/', views.AssetListView.as_view(), name='asset_list'),
    path('assets/<int:pk>/', views.AssetDetailView.as_view(), name='asset_detail'),
    path('assets/create/', views.AssetCreateView.as_view(), name='asset_create'),
    path('assets/<int:pk>/update/', views.AssetUpdateView.as_view(), name='asset_update'),
    path('assets/<int:pk>/delete/', views.AssetDeleteView.as_view(), name='asset_delete'),

    # Location URLs
    path('locations/', views.LocationListView.as_view(), name='location_list'),
    path('locations/<int:pk>/', views.LocationDetailView.as_view(), name='location_detail'),
    path('locations/create/', views.LocationCreateView.as_view(), name='location_create'),
    path('locations/<int:pk>/update/', views.LocationUpdateView.as_view(), name='location_update'),
    path('locations/<int:pk>/delete/', views.LocationDeleteView.as_view(), name='location_delete'),

    # AssetLocation URLs
    path('movements/', views.AssetLocationListView.as_view(), name='assetlocation_list'),
    path('movements/create/', views.AssetLocationCreateView.as_view(), name='assetlocation_create'),
    path('movements/<int:pk>/update/', views.AssetLocationUpdateView.as_view(), name='assetlocation_update'),
    path('movements/<int:pk>/delete/', views.AssetLocationDeleteView.as_view(), name='assetlocation_delete'),
]
