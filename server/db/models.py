from django.db import models

# Create your models here.


class User(models.Model):
    email_txt = models.CharField(max_length=100, primary_key=True)
    wallet = models.IntegerField(default=None)
    balance = models.FloatField(max_length=None, default=None)

    def __str__(self):
        return self.wallet
    pass


class Picture(models.Model):
    wallet = models.ForeignKey(User, on_delete=models.PROTECT)
    picture_binary = models.BinaryField(max_length=None)
    category = models.CharField(max_length=10, default=None)

    def __str__(self):
        return self.picture_binary
    pass
