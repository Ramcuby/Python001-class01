from django.db import models

# Create your models here.

class Cellphone(models.Model):
    id = models.BigAutoField(primary_key = True)
    date = models.CharField(max_length = 30)
    n_star = models.IntegerField()
    estimate = models.CharField(max_length=200)
    sentiment = models.DecimalField(max_digits=11,decimal_places = 10)
    
    class Meta:
        managed = False
        db_table = 'cellphone' #很奇怪，加上这个后Cellphone才有数据
