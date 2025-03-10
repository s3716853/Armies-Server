from django.db import models

# https://docs.djangoproject.com/en/5.1/topics/db/models/

class User(models.Model):
    # TODO: chuck in a config file
    user_name = models.CharField(max_length=30)
    
    # Stringify
    def __str__(self):
        return f"ui:{self.id} - user_name:{self.user_name}"