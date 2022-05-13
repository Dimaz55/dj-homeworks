from pprint import pprint

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement, AdvertisementStatusChoices, \
    Favourite


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )
    add_to_favourites = serializers.SerializerMethodField()
    view_favourites = serializers.SerializerMethodField()

    class Meta:
        model = Advertisement
        fields = ('id', 'add_to_favourites', 'view_favourites', 'title',
                  'description', 'creator', 'status', 'created_at',)

    def get_add_to_favourites(self, obj):
        if obj.creator != self.context["request"].user:
            return f'POST /advertisements/{obj.id}/fav/'
        return 'недоступно для автора объявления'

    def get_view_favourites(self, obj):
        return 'GET /favs/'

    def create(self, validated_data):
        """Метод для создания"""
        validated_data["creator"] = self.context["request"].user
        self.validate(validated_data)
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        action = self.context['request']._request.method
        open_adv_count = Advertisement.objects \
                .filter(creator=self.context["request"].user) \
                .filter(status=AdvertisementStatusChoices.OPEN) \
                .count()
        if open_adv_count == 10:
            if action == 'POST' or \
               action == 'PATCH' and data['status'] == 'OPEN':
                raise ValidationError('Ограничение 10 открытых объявлений')
        return data


class FavAdvListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator', 'status',
                  'created_at',)


class FavAdvertisementSerializer(serializers.ModelSerializer):
    ad = FavAdvListSerializer(read_only=True)
    delete_from_favourites = serializers.SerializerMethodField()

    class Meta:
        model = Favourite
        fields = ['id', 'delete_from_favourites', 'ad']

    def get_delete_from_favourites(self, obj):
        return f'DELETE /favs/{obj.id}/'
