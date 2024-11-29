from django.shortcuts import render
from django.http import HttpResponse
from .forms import RobotForm

# Create your views here.
def robot_form_request(request):
    if request.method == "GET":
        form = RobotForm()
        return render(request, "robot_form.html", {"form" : form}, status=200)
    elif request.method == "POST":
        form = RobotForm(request.POST)
        if form.is_valid():
            form.save()
            # If we saved the form we print a success message.
            return HttpResponse("Created a robot!", status=200)
        # If we got here form was not valid so we return 400
        return HttpResponse("Could not create a robot.", status=400)
    else:
        return HttpResponse("Bad request.", status=400)