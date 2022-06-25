from django.urls import path
from .views import ListAllGame, GamesReUpDeView

urlpatterns = [

    path('listofgames', ListAllGame.as_view(), name='list_create_ListAllGame'),
    path('<pk>', GamesReUpDeView.as_view(), name='retrieve_update_delete')
    
]
# path('', ListAllGameReview.as_view(), name='list_create_ListAllGameReview'),
    # path('', ListAllGameLicense.as_view(), name='list_create_ListAllGameLicense'),

    # path('<pk>', ExpenseReUpDeView.as_view(), name='retrieve_update_delete')
    # l
