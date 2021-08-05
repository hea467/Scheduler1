from django.shortcuts import render, HttpResponse, redirect

from .models import Event
from .forms import EventForm

# Create your views here.

# lis = []
# for event in events:
# lis.append(event.start_time)


def index(request):
    events = Event.objects.all()
    context = {"events": events}
    return render(request, "project/index.html", context)


def main(request):

    # events = Event.objects.order_by("start_time")
    events = ["event_alpha: ", "event_beta: --"]
    results = [1, 2, 3]
    context = {"events": events, "results": results}
    return render(request, "project/main.html", context)


def new_event(request):
    """Add a new event"""
    if request.method != "POST":
        # The case where no data is submitted
        form = EventForm()  # Spawn an empty instance
    else:
        # The case where POST data is submitted
        form = EventForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("project:main")
    context = {"form": form}
    return render(request, "project/new_event.html", context)
