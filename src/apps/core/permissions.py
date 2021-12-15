from rest_framework import permissions


class IsSelf(permissions.BasePermission):
    """
    Object-level permission to only allow ones self access.
    """

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        if hasattr(obj, 'created_by'):
            return obj.created_by == request.user
        if hasattr(obj, 'user'):
            return obj.user == request.user

        return obj == request.user
