from django.db import models
from django.contrib.auth.models import  AbstractUser
# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=99, unique=True)
    email = models.EmailField(('email address') ,max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_deleted = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    class Meta:
        db_table = "User"
    
    