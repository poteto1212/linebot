from django.db import models

class Message(models.Model):
    medicine=models.CharField(verbose_name="薬品名",max_length=50)
    detail=models.TextField(verbose_name="特徴")
    
    def __str__(self):
        return self.medicine
    
    class Meta:
        verbose_name_plural="医薬品の特徴"

# Create your models here.
