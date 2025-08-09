from rest_framework import permissions


class CanViewApplications(permissions.BasePermission):
    """
    Allow job owners and admins to view all applications.
    Other authenticated users can only create.
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if view.action == 'create':
            return True

        if view.action in ['list', 'retrieve']:
            return request.user.is_staff or request.user.is_superuser

        return False
