from django.db import models


class Post(models.Model):
    date = models.DateField(db_column='Дата')
    title = models.CharField(max_length=100, db_column='Название')
    amount = models.IntegerField(db_column='Количество')
    distance = models.DecimalField(max_digits=11, decimal_places=2, db_column='Расстояние')

    class Meta:
        ordering = ['title']
