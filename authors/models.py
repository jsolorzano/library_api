from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=150)
  birthday = models.DateField(blank=True, null=True)
  created_date = models.DateTimeField(default=timezone.now)

  class Meta:
    ordering = ['name']
    
  def __str__(self):
        return self.name
