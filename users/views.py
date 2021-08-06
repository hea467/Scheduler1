from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Thank god for django methods


def register(request):
    # POST and GET are the two main possible methods
    # If the user is not posting data...
    if request.method != "POST":
        # Create a user
        form = UserCreationForm()
    else:
        # Now we are posting... the data would be the form
        # We need to process the form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log that user in with their new account
            login(request, new_user)
            return redirect("project:index")

    context = {"form": form}
    return render(request, "registration/register.html", context)
