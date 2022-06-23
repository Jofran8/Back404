from rest_framework import serializers
from .models import Game, GameReview, GameLicense

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
   

