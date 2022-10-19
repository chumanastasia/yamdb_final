from rest_framework import permissions


class AdminOrReadOnlyPermission():
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_superuser
            or (
                request.user.is_authenticated
                and request.user.is_admin
            )
        )

    def has_object_permission(self, request, view, obj):
        return True


class IsAdminOrSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_admin or request.user.is_superuser)


class IsAdminIsAuthorIsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if (
                request.user.is_staff
                or request.user.role == 'admin'
                or request.user.role == 'moderator'
                or obj.author == request.user
            ):
                return True
        elif request.method in permissions.SAFE_METHODS:
            return True
        return None
