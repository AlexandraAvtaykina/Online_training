from rest_framework.permissions import BasePermission


class IsManager(BasePermission):

    def has_permission(self, request, view):
        return not request.user.is_staff


class IsAutor(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user.is_staff
