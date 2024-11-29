from django.shortcuts import render
from django.http import HttpResponse
from .forms import RobotForm

# Create your views here.
def robot_form_request(request):
    if request.method == "GET":
        form = RobotForm()
        return render(request, "robot_form.html", {"form" : form}, status=200)
    elif request.method == "POST":
        pass
    else:
        return HttpResponse("Bad request.", status=400)