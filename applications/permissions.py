from rest_framework import permissions


class CanViewApplications(permissions.BasePermission):
    def has_permission(self, request, view):
        # Must be authenticated for anything
        if not request.user or not request.user.is_authenticated:
            return False

        # Allow create and list for all logged in users
        if view.action in ['create', 'list', 'retrieve']:
            return True

        # Allow update/delete only for admins
        if view.action in ['update', 'partial_update', 'destroy']:
            return request.user.is_staff or request.user.is_superuser

        return False

    def has_object_permission(self, request, view, obj):
        # Admins can do anything
        if request.user.is_superuser:
            return True

        # Applicants can view/update/delete their own applications if you want
        # Otherwise restrict updates etc.
        if view.action in ['retrieve']:
            return obj.applicant == request.user

        # Restrict edits/deletes to admins only (optional)
        return False
