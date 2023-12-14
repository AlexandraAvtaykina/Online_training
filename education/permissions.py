from rest_framework.permissions import BasePermission


class IsManager(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff and request.user == request.get_object().author:
            return True
        return False


class IsAutor(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_staff and request.user == request.get_object().author:
            return True
        return False
