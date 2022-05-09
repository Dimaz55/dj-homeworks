from rest_framework.permissions import BasePermission

from advertisements.models import AdvertisementStatusChoices


class IsCreator(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user


class IsDraftCreator(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(13, obj)
        return obj.status == AdvertisementStatusChoices.DRAFT and \
               obj.creator == request.user
