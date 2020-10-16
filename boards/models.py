# Django
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Board(models.Model):
    board_size = models.IntegerField(validators=[MaxValueValidator(12), MinValueValidator(8)])

    def __str__(self):
        return self.board_size

    def get_size(self):
        return 'The board size is ' + str(self.board_size)
