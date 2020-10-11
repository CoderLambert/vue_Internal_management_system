from rest_framework.permissions import BasePermission


class IsAdminOrArticalOwner(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH", "DELETE"]:
            return bool(request.user == obj.user or request.user.is_staff)
        else:
            return True


