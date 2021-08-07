from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Event, Blog
from .forms import EventForm, BlogForm


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
    maximized_event = []
    events = list(Event.objects.filter(owner=request.user).order_by("end_time"))
    invalid_events = []
    for event in events:
        if (
            event.start_time > 24
            or event.end_time > 24
            or event.end_time < 0
            or event.start_time < 0
        ):
            events.remove(event)
            invalid_events.append(event)
    if len(events) == 0:
        context = {"events": maximized_event, "invalid_events": invalid_events}
        return render(request, "project/main.html", context)
    else:
        k = 0
        maximized_event.append(events[k])
        for i in range(1, len(events)):
            st = events[i].start_time
            if st >= events[k].end_time:
                maximized_event.append(events[i])
                k = i
        context = {"events": maximized_event, "invalid_events": invalid_events}
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
            return redirect("project:listevents")
    context = {"form": form}
    return render(request, "project/new_event.html", context)


def blog(request):
    """A shared blog site for students to share their learning progress"""
    blogs = Blog.objects.order_by("topic")
    context = {"blogs": blogs}
    return render(request, "project/blogs.html", context)


@login_required
def newblog(request):
    """Page to add new blogs"""
    if request.method != "POST":
        # The case where no data is submitted
        form = BlogForm()  # Spawn an empty instance
    else:
        # The case where POST data is submitted
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("project:blog")
    context = {"form": form}
    return render(request, "project/newblog.html", context)


def delete(request):
    Event.objects.filter(owner=request.user).delete()
    return redirect("project:listevents")


def editevent(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method != "POST":
        form = EventForm(instance=event)
    else:
        form = EventForm(instance=event, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("project:listevents")

    context = {"event": event, "form": form}
    return render(request, "project/editevent.html", context)


def deleteevent(request, event_id):
    Event.objects.filter(owner=request.user).filter(id=event_id).delete()
    return redirect("project:listevents")