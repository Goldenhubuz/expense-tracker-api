from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.models import TimeStampedModel
User = get_user_model()


# Create your models here.
class Task(TimeStampedModel):
    description = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Task {self.id} - {self.description}"