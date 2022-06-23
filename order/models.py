from django.db import models
from authentication.models import User
from games.models import Game, GameLicense


# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    user = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name='user_order'
    )

    game = models.ForeignKey(
        Game,
        on_delete=models.RESTRICT,
        related_name='game_order'
    )

    license = models.OneToOneField(
        GameLicense,
        on_delete=models.RESTRICT,
        related_name='license_order'
    )

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return self.price
