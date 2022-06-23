from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .serializers import OrderSerializers
from .models import Order
# Create your views here.
class OrderListCreateView(ListCreateAPIView):
    serializer_class = OrderSerializers
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        # user -> request.user
        return serializer.save(user=self.request.user.id)

    def get_queryset(self):
        # user -> request.user
        return self.queryset.filter(user=self.request.user.id)

class OrderReUpDeView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializers
    queryset = Order.objects.all()
    # permission_classes = [permissions.IsAuthenticated, IsUser]
