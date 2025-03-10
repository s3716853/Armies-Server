from django.db import models
from models.user import User

class GameState(models.Model):
    # TODO: chuck in a config file
    map = models.JSONField
    turn = models.IntegerField
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Stringify
    def __str__(self):
        return f"ui:{self.id} - user_id:{self.user.id} - turn:{self.turn} - maps:{str(self.map)}"