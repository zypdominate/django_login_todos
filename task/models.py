from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    text = models.CharField(max_length=200)

    completed =models.BooleanField(default=False)
    # 使用外键, 建立Task 和 User 的关联
    creator =models.ForeignKey(to=User,on_delete=True)