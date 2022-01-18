from .models import Author
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    # ~ fields = '__all__'
    fields = ['id', 'name', 'birthday']

