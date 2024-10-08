from django.shortcuts import render

from polls.models import Question


# Create your views here.
def home(request):
    questions = Question.objects.all()
    return render(
        request,
        "home/home.html",
        {
            "questions": questions,
        },
    )
