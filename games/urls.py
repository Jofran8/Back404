from django.urls import path
from .views import ListAllGame, GamesReUpDeView, ListAllGameLicense

urlpatterns = [

    path('listofgames', ListAllGame.as_view(), name='list_create_ListAllGame'),
    path('<pk>', GamesReUpDeView.as_view(), name='retrieve_update_delete'),
    path('license', ListAllGameLicense.as_view(), name='list_create_ListAllGameLicense'),
    
]
# path('', ListAllGameReview.as_view(), name='list_create_ListAllGameReview'),

    # path('<pk>', ExpenseReUpDeView.as_view(), name='retrieve_update_delete')
    # l
