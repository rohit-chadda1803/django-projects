from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=200 )  # note heading 
    content = models.TextField(default = "", blank=True , null= True )
   

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title ; 


"""
my concern : 
user --> username , email, pass 
"""