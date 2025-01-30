from django.db import models
from django.contrib.auth.models import User
import datetime

class tag(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return u'{0}'.format(self.name)

class entry(models.Model):
    content = models.TextField(max_length=500, default="New entry")
    entry_time = models.DateTimeField(default=datetime.datetime.now)
    deadline = models.DateField(default=datetime.datetime.now)
    tag = models.ForeignKey(tag, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=False)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
