from django.urls import path
from .views import OrderListCreateView, OrderReUpDeView

urlpatterns = [
    path('', OrderListCreateView.as_view(), name='list_order'),
    # path('<pk>', OrderReUpDeView.as_view(), name='retrieve_update_delete')
]

