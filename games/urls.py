from django.urls import path
from .views import ListAllGame, GamesReUpDeView, LicenseListCreateView, BuyGamesView

urlpatterns = [

    path('listofgames', ListAllGame.as_view(), name='list_create_ListAllGame'),
    path('<pk>', GamesReUpDeView.as_view(), name='retrieve_update_delete'),
    path('licences/License', LicenseListCreateView.as_view(), name='license_create_view'),
    path('buygame/', BuyGamesView.as_view(), name='buy_game')
    
]
# path('', ListAllGameReview.as_view(), name='list_create_ListAllGameReview'),
    # path('', ListAllGameLicense.as_view(), name='list_create_ListAllGameLicense'),

    # path('<pk>', ExpenseReUpDeView.as_view(), name='retrieve_update_delete')
    # l
