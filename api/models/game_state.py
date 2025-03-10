from django.db import models
from .user import User
import json

# https://docs.djangoproject.com/en/5.1/topics/db/examples/many_to_one/
# https://docs.djangoproject.com/en/5.1/topics/db/models/

class GameState(models.Model):
    # TODO: chuck in a config file
    map = models.JSONField()
    turn = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Stringify
    def __str__(self):
        map_string = json.dumps(self.map)
        return f"ui:{self.id} - user_id:{self.user.id} - turn:{self.turn} - maps:{map_string}"