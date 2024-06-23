
from rest_framework import permissions

class IsHostelOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role=="hostelowner")

class IsWarden(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role=="warden")


class IsHostelOwnerOrWarden(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and (
            request.user.role == 'hostelowner' or 
            request.user.role == 'warden'
        ))