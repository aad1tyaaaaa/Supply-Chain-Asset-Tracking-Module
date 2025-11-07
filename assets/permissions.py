from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import Group
from django.shortcuts import redirect


class RoleRequiredMixin(AccessMixin):
    """Require user to belong to at least one of the given groups.

    Usage: set `required_groups = ['admin', 'manager']` on the view.
    """
    required_groups = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if not self.required_groups:
            return super().dispatch(request, *args, **kwargs)

        user_groups = set(request.user.groups.values_list('name', flat=True))
        if user_groups.intersection(set(self.required_groups)) or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        # Redirect to login page or show forbidden
        return redirect('dashboard')
