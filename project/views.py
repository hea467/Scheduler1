from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Event
from .forms import EventForm


def index(request):
    return render(request, "project/index.html")


@login_required
def listevents(request):
    events = Event.objects.filter(owner=request.user).all()
    # Just an extra layer of protection for some clever hackers ;)
    for event in events:
        if event.owner != request.user:
            raise Http404
    context = {"events": events}
    return render(request, "project/listevents.html", context)


@login_required
def main(request):

    # events = Event.objects.order_by("start_time")
    events = Event.objects.filter(owner=request.user).order_by("start_time")
    context = {"events": events}
    return render(request, "project/main.html", context)


@login_required
def new_event(request):
    """Add a new event"""
    if request.method != "POST":
        # The case where no data is submitted
        form = EventForm()  # Spawn an empty instance
    else:
        # The case where POST data is submitted
        form = EventForm(data=request.POST)
        if form.is_valid():
            new_event = form.save(commit=False)
            new_event.owner = request.user
            new_event.save()
            return redirect("project:main")
    context = {"form": form}
    return render(request, "project/new_event.html", context)
