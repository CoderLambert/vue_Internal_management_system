from rest_framework.permissions import BasePermission


class IsAdminOrProjectMember(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        # 用来判断针对的obj权限：
        # 例如：是不是某一个人的评论
        '''
        只有评论人是自己才能删除选定的评论
        '''
        if request.method in ["PUT", "PATCH", "DELETE"]:
            return bool(request.user in obj.member.all() or request.user.is_staff)

        elif request.method in ["DELETE"]:
            return bool(request.user.is_staff)
        else:
            return True


from rest_framework.permissions import BasePermission


class IsAdminOrMachineOwner(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        # 用来判断针对的obj权限：
        # 例如：是不是某一个人的评论
        '''
        只有评论人是自己才能删除选定的评论
        '''
        if request.method in ["PUT", "PATCH", "DELETE"]:
            return bool(request.user == obj.user or request.user.is_staff)

        elif request.method in ["DELETE"]:
            return bool(request.user.is_staff)
        else:
            return True
