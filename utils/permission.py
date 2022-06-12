from rest_framework import permissions

class CustomReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff


class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_staff


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin