from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class NoteType(models.Model):
    name = models.CharField(max_length=55)
   

class Note(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    type = models.ForeignKey(NoteType,on_delete=models.SET_NULL,null=True)
    User = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    
