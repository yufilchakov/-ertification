from rest_framework.permissions import BasePermission


class IsActive(BasePermission):
    """Разрешение для активных сотрудников."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_active_employee
