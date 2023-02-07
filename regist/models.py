
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class ResetCode(models.Model):
    code = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    valid_until = models.DateTimeField()
# Create your models here.
