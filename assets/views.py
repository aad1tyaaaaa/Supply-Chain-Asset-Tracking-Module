from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Count, Sum, Prefetch
from django.views.decorators.cache import cache_page
from .models import Asset, Location, AssetLocation
from .forms import AssetForm, LocationForm, AssetLocationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .permissions import RoleRequiredMixin

# Asset CRUD Views
class AssetListView(LoginRequiredMixin, ListView):
    model = Asset
    template_name = 'assets/asset_list.html'
    context_object_name = 'assets'
    paginate_by = 10

    def get_queryset(self):
        # Assets have no FK fields; ordering only. Keep queryset lean for large datasets.
        return Asset.objects.only('id', 'name', 'value', 'created_at').order_by('-created_at')

class AssetDetailView(LoginRequiredMixin, DetailView):
    model = Asset
    template_name = 'assets/asset_detail.html'
    context_object_name = 'asset'

    def get_queryset(self):
        # Prefetch recent location history and related location in a single query.
        return Asset.objects.prefetch_related(
            Prefetch('locations', queryset=AssetLocation.objects.select_related('location').only('id', 'asset_id', 'location_id', 'timestamp'))
        ).all()

class AssetCreateView(RoleRequiredMixin, LoginRequiredMixin, CreateView):
    model = Asset
    form_class = AssetForm
    template_name = 'assets/asset_form.html'
    success_url = reverse_lazy('asset_list')
    required_groups = ['manager', 'admin']

class AssetUpdateView(RoleRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Asset
    form_class = AssetForm
    template_name = 'assets/asset_form.html'
    success_url = reverse_lazy('asset_list')
    required_groups = ['manager', 'admin']

class AssetDeleteView(RoleRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Asset
    template_name = 'assets/asset_confirm_delete.html'
    success_url = reverse_lazy('asset_list')
    required_groups = ['admin']

# Location CRUD Views
class LocationListView(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'assets/location_list.html'
    context_object_name = 'locations'
    paginate_by = 10

    def get_queryset(self):
        # Count distinct assets at each location and prefetch a small set of related rows.
        return Location.objects.prefetch_related(
            Prefetch('assets', queryset=AssetLocation.objects.select_related('asset').only('id', 'asset_id', 'location_id', 'timestamp'))
        ).annotate(
            asset_count=Count('assets__asset', distinct=True)
        ).order_by('name')

class LocationDetailView(LoginRequiredMixin, DetailView):
    model = Location
    template_name = 'assets/location_detail.html'
    context_object_name = 'location'

    def get_queryset(self):
        return Location.objects.prefetch_related(
            Prefetch('assets', queryset=AssetLocation.objects.select_related('asset').only('id', 'asset_id', 'location_id', 'timestamp'))
        ).all()

class LocationCreateView(RoleRequiredMixin, LoginRequiredMixin, CreateView):
    model = Location
    form_class = LocationForm
    template_name = 'assets/location_form.html'
    success_url = reverse_lazy('location_list')
    required_groups = ['manager', 'admin']

class LocationUpdateView(RoleRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Location
    form_class = LocationForm
    template_name = 'assets/location_form.html'
    success_url = reverse_lazy('location_list')
    required_groups = ['manager', 'admin']

class LocationDeleteView(RoleRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Location
    template_name = 'assets/location_confirm_delete.html'
    success_url = reverse_lazy('location_list')
    required_groups = ['admin']

# AssetLocation CRUD Views
class AssetLocationListView(LoginRequiredMixin, ListView):
    model = AssetLocation
    template_name = 'assets/assetlocation_list.html'
    context_object_name = 'assetlocations'
    paginate_by = 10

    def get_queryset(self):
        # Use select_related to avoid extra queries when showing asset/location per movement
        return AssetLocation.objects.select_related('asset', 'location').only('id', 'asset_id', 'location_id', 'timestamp').order_by('-timestamp')

class AssetLocationCreateView(RoleRequiredMixin, LoginRequiredMixin, CreateView):
    model = AssetLocation
    form_class = AssetLocationForm
    template_name = 'assets/assetlocation_form.html'
    success_url = reverse_lazy('assetlocation_list')
    required_groups = ['manager', 'admin']

class AssetLocationUpdateView(RoleRequiredMixin, LoginRequiredMixin, UpdateView):
    model = AssetLocation
    form_class = AssetLocationForm
    template_name = 'assets/assetlocation_form.html'
    success_url = reverse_lazy('assetlocation_list')
    required_groups = ['manager', 'admin']

class AssetLocationDeleteView(RoleRequiredMixin, LoginRequiredMixin, DeleteView):
    model = AssetLocation
    template_name = 'assets/assetlocation_confirm_delete.html'
    success_url = reverse_lazy('assetlocation_list')
    required_groups = ['admin']

# Dashboard View
@login_required
@cache_page(60)  # cache dashboard for 60 seconds (can be tuned or disabled via cache backend)
def dashboard(request):
    # Aggregations done in the database for efficiency.
    total_assets = Asset.objects.count()
    total_locations = Location.objects.count()
    total_movements = AssetLocation.objects.count()
    total_value = Asset.objects.aggregate(total=Sum('value'))['total'] or 0

    # Recent movements (only latest 10) with related asset and location loaded.
    recent_movements = AssetLocation.objects.select_related('asset', 'location').only('id', 'asset_id', 'location_id', 'timestamp').order_by('-timestamp')[:10]

    # Assets per location (distinct asset count) - returns top 5 locations
    assets_per_location = Location.objects.annotate(asset_count=Count('assets__asset', distinct=True)).order_by('-asset_count')[:5]

    context = {
        'total_assets': total_assets,
        'total_locations': total_locations,
        'total_movements': total_movements,
        'total_value': total_value,
        'recent_movements': recent_movements,
        'assets_per_location': assets_per_location,
    }
    return render(request, 'assets/dashboard.html', context)
