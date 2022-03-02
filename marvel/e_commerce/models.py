from django.db import models

from django.contrib.auth.models import User




class Comic(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    marvel_id = models.PositiveIntegerField(
        verbose_name='marvel ids', default=1, unique=True)
    title = models.CharField(
        verbose_name='titles', max_length=120, default='')
    description = models.TextField(
        verbose_name='descriptions', default='')
    price = models.FloatField(
        verbose_name='prices', max_length=5, default=0.00)
    stock_qty = models.PositiveIntegerField(
        verbose_name='stock qty', default=0)
    picture = models.URLField(
        verbose_name='pictures', default='')

    class Meta:
            db_table = 'e_commerce_comics'

    def __str__(self):
        return f'{self.id}'
    
class WhishList(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    marvel_id = models.PositiveIntegerField(verbose_name='marvel_ids', default=1, unique=True)
    user_id = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    comic_id = models.ForeignKey(to=Comic, verbose_name='Comic', on_delete=models.DO_NOTHING, default=1, blank=True)
    favorite = models.BooleanField(default=True)
    cart = models.BooleanField(default=True)
    whished_qty = models.PositiveIntegerField(default=0)
    buied_qty = models.PositiveIntegerField(default=0)
    
    class Model:
        verbose_name_plural = 'whislists'
        
    def __str__(self):
        return f'{self.favorite}'