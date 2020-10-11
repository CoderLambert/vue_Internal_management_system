from rest_framework.permissions import BasePermission


class IsAdminOrOwner(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(request.user or request.user.is_staff)


    def has_object_permission(self, request, view, obj):
        # 用来判断针对的obj权限：
        '''
        只有是自己才能删除选定的站点
        '''

        if request.method in ["PUT", "PATCH", "DELETE"]:
            return bool(request.user == obj.owner)
        else:
            return True
