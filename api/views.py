from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.http import HttpRequest
import json

from api.models.user import User
from api.models.game_state import GameState


def retrieve(request : HttpRequest):
    users = User.objects.all()
    game_states = GameState.objects.all()
    
    return_object = {
        "users": serializers.serialize("json", users),
        "game_states": serializers.serialize("json", game_states)
    }
    
    data = json.dumps(return_object)
    
    return HttpResponse(data, content_type="application/json")


def upload(request : HttpRequest):
    return _debug_upload(request)
    
    
def _debug_upload(request : HttpRequest):
    print("BODY")
    print(request.body)
    print("HEADERS")
    print(request.headers)
    
    last_user_id = User.objects.count() + 1
    new_username = f"User-{last_user_id}"
    user = User.objects.create(user_name = new_username)
    user.save()
      
    map_string = f'{{"user":{user.id}}}'
    map = GameState.objects.create(user=user, turn=3, map=json.loads(map_string))
    map.save()
    
    user_string = str(user)
    map_string = str(map)
    print(user_string)
    print(map_string)
    
    return_object = {
        "user": user_string,
        "map": map_string
    }
    
    data = json.dumps(return_object)
    
    return HttpResponse(data, content_type="application/json")
    
    
"""
Verifies the request object has all fields and is correct
"""
def _verify_request_object(request):
    return True
