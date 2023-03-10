from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

@login_required
def room(request, room_name):
    print(room_name)
    print(mark_safe(json.dumps(room_name)))
    return render(request, 'chat/room.html', {
        'room_name_json': room_name,
        'username': request.user.username,
    })
