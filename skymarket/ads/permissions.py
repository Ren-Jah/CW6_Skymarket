from rest_framework import permissions

from users.models import UserRoles


class IsOwner(permissions.BasePermission):
    message = 'Редактировать и удалять может только владелец.'

    def has_object_permission(self, request, view, obj):
        if request.user.role == obj.owner:
            return True
        return False


class IsStaff(permissions.BasePermission):
    message = 'Вы не являетесь админом.'

    def has_object_permission(self, request, view, obj):
        if request.user.role == UserRoles.ADMIN:
            return True
        return False
