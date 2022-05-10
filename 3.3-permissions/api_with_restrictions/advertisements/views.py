from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement, Favourite, \
    AdvertisementStatusChoices
from advertisements.permissions import IsDraftCreator, \
    IsCreatorOrAdminUser
from advertisements.serializers import AdvertisementSerializer, \
    FavAdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        q = Q(status=AdvertisementStatusChoices.DRAFT) &\
            ~Q(creator=self.request.user)
        return queryset.exclude(q)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsCreatorOrAdminUser()]
        else:
            return [IsDraftCreator()]

    @action(methods=['POST'], detail=True)
    def fav(self, request, pk):
        ad = Advertisement.objects.get(pk=pk)
        if ad.creator == request.user:
            raise ValidationError('Вы не можете добавлять свои объявления в '
                                  'избранное')
        Favourite.objects.create(creator=request.user, ad=ad)
        return Response({'detail': f'Объявление №{pk} добавлено в избранное'})


class FavAdvertisementViewSet(ModelViewSet):
    """ViewSet для избранных объявлений."""
    http_method_names = ['get', 'delete']
    queryset = Favourite.objects.all()
    serializer_class = FavAdvertisementSerializer
    permission_classes = [IsCreatorOrAdminUser]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(creator=self.request.user)
