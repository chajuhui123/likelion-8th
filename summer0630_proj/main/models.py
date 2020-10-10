from django.db import models

# Create your models here.
class Members(models.Model):
    memberId = models.IntegerField(primary_key = True)
    memberName = models.CharField(max_length = 127)
    home = models.CharField(max_length=1023)

class Orders(models.Model):
    memberId = models.ForeignKey(Members, on_delete = models.SET_NULL, null = True, blank = True)
    orderId = models.IntegerField(primary_key = True)

class Goods(models.Model):
    goodsName = models.CharField(max_length = 127)
    goodsId = models.IntegerField(primary_key = True)
    goodsCost = models.IntegerField()
    orderId = models.ForeignKey(Orders, on_delete = models.SET_NULL, null = True, blank = True)

class Sheets(models.Model):
    orderId = models.ForeignKey(Orders, on_delete = models.SET_NULL, null = True, blank = True)
    goodsId = models.ForeignKey(Goods, on_delete = models.SET_NULL, null = True, blank = True)
    memberId = models.ForeignKey(Members, on_delete = models.SET_NULL, null = True, blank = True)