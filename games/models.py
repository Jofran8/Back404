from django.db import models
from authentication.models import User


# Create your models here.
class Game(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.CharField(max_length=255)
    image_frontpage = models.CharField(max_length=255)
    mode = models.TextField()
    platforms = models.TextField()
    genre = models.TextField()
    description = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'games'

    def __str__(self):
        return self.name


class GameReview(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField()
    recommended = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name='user'
    )

    game = models.ForeignKey(
        Game,
        on_delete=models.RESTRICT,
        related_name='game'
    )

    class Meta:
        db_table = 'games_reviews'

    def __str__(self):
        return self.message


class GameLicense(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    game = models.ForeignKey(
        Game,
        on_delete=models.RESTRICT,
        related_name='game_license'
    )

    class Meta:
        db_table = 'games_licenses'

    def __str__(self):
        return self.key
