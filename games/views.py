from logging import raiseExceptions
from urllib import response
from requests import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import permissions, status

from .serializers import GameSerializers, GameReviewSerializers, GameLicenseSerializers, BuyGameSerializers
from .models import Game, GameReview, GameLicense
from order.models import Order


class ListAllGame(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializers

class GamesReUpDeView(RetrieveUpdateDestroyAPIView):
    serializer_class = GameSerializers
    queryset = Game.objects.all()
# class GameReviewListCreateView(ListCreateAPIView):
#     serializer_class = GameReviewSerializers
#     queryset = GameReview.objects.all()

#     # Creación, injectar al usuario
#     def perform_create(self, serializer):
#         # user -> request.user
#         return serializer.save(user=self.request.user.id)

#     # Listado
#     def get_queryset(self):
#         # user -> request.user
#         return self.queryset.filter(user=self.request.user.id)




    # permission_classes = [permissions.IsAuthenticated, IsUser]
# class GetGameById(RetrieveAPIView):
#     queryset = Game.objects.all()
#     serializer_class = GameSerializers

# class ListAllGameReview(ListAPIView):
#     queryset = GameReview.objects.all()
#     serializer_class = GameReviewSerializers


# class GetGameReviewById(RetrieveAPIView):
#     queryset = GameReview.objects.all()
#     serializer_class = GameReviewSerializers

#class ListAllGameLicense(ListAPIView):
#   queryset = GameLicense.objects.all()
#   serializer_class = GameLicenseSerializers


#class GetGameLicenseById(RetrieveAPIView):
#    queryset = GameLicense.objects.all()
#    serializer_class = GameLicenseSerializers

class LicenseListCreateView(ListCreateAPIView):
    serializer_class = GameLicenseSerializers
    queryset = GameLicense.objects.all()

    #def perform_create(self, serializer):
    #    return serializer.save(user=self.request.user)

    #def get_queryset(self):
    #    return self.queryset.filter(user=self.request.user)

class BuyGamesView(CreateAPIView):
    serializer_class = BuyGameSerializers
    queryset = Order.objects.all()

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'python'})
