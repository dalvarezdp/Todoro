from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Task(models.Model):

    PENDING = "PEN"
    DONE = "DON"
    STATUSES = (
        (PENDING,"Pending"),
        (DONE,"Done")
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    status = models.CharField(max_length=3, default=PENDING, choices=STATUSES)
    time_estimated = models.IntegerField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) #Añade automáticamente la fecha de creación
    modified_at = models.DateTimeField(auto_now=True) #Actualiza la fecha al guardar automáticamente
    owner = models.ForeignKey(User, related_name="owned_tasks")
    assignee = models.ForeignKey(User, related_name="assigned_tasks", null=True, default=None)

    def __str__(self):
        return self.name