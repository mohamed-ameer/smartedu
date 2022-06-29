from email import message
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Message, Room
from .forms import RoomForm
from .filters import RoomFilter
@login_required
def rooms(request):
    rooms = Room.objects.all()
    myFilter=RoomFilter(request.GET,queryset=rooms)
    rooms =myFilter.qs
    return render(request, 'room/rooms.html', {'rooms': rooms,'myFilter':myFilter})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages=Message.objects.filter(room=room)[0:25]
    return render(request, 'room/room.html', {'room': room,'messages': messages})


def NewRoom(request):
    user = request.user
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            Room.objects.create(name=name,user=user)
            return redirect('rooms')
    else:
        form = RoomForm()
    
    context = {
        'form': form,
    }

    return render(request, 'room/newroom.html', context)
