from django.db import models
import sys
sys.path.append("..")
# Create your models here.
    
class MessageHistory(models.Model):
    topic = models.CharField(max_length=128)
    message = models.TextField()
    date = models.DateTimeField()