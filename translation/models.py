from django.db import models

# Create your models here.
# Interact with database.
class DCItem(models.Model):
    content = models.TextField()
    gen = models.TextField()

class TodoItem(models.Model):
    content = models.TextField()
    gen = models.TextField()

class UnmtItem(models.Model):
    content = models.TextField()
    gen = models.TextField()
