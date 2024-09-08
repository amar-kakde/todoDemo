from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoModel(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    todo        = models.CharField(max_length=255)
    description = models.CharField(max_length=526)
    status      = models.BooleanField(default=False)
    created     = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['created']
    
    def __str__(self):
        return self.todo