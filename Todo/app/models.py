from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=40)
    date = models.DateField("Date", default=datetime.date.today)
    time = models.TimeField(default=datetime.datetime.now().time())
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.text,self.date,self.time