from rest_framework.permissions import BasePermission

from advertisements.models import AdvertisementStatusChoices


class IsCreatorOrAdminUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user or \
               bool(request.user and request.user.is_staff)


class IsDraftCreator(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.status == AdvertisementStatusChoices.DRAFT and \
               obj.creator == request.user or request.user
