from rest_framework import serializers
from .models import Game, GameReview, GameLicense
from order.models import Order

class GameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
        # [
        #     'id',
        #     'name',
        #     'price',
        #     'image',
        #     'image_frontpage',
        #     'mode',
        #     'platforms',
        #     'genre',
        #     'description',
        #     'status',
        # ]
class GameReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = GameReview
        fields = '__all__'
        # [
        #     'id',
        #     'message',
        #     'recommended',
        #     'status',
        # ]
class GameLicenseSerializers(serializers.ModelSerializer):
    class Meta:
        model = GameLicense
        fields = '__all__'
        # [
        #     'id',
        #     'key',
        #     'active',
        # ]

class BuyGameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

