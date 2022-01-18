from django.db import models
from django.utils import timezone
from authors.models import Author

# Create your models here.
class Book(models.Model):
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  title = models.CharField(max_length=150)
  year = models.CharField(max_length=10)
  created_date = models.DateTimeField(default=timezone.now)

  class Meta:
    ordering = ['title']
    
  def __str__(self):
        return self.title
