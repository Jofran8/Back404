from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework import permissions

from .serializers import GameSerializers, GameReviewSerializers, GameLicenseSerializers
from .models import Game, GameReview, GameLicense


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

# class ListAllGameLicense(ListAPIView):
#     queryset = GameLicense.objects.all()
#     serializer_class = GameLicenseSerializers


# class GetGameLicenseById(RetrieveAPIView):
#     queryset = GameLicense.objects.all()
#     serializer_class = GameLicenseSerializers

