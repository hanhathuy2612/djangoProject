from django.shortcuts import render

from polls.models import Question


def home(request):
    questions = Question.objects.all()
    return render(
        request,
        "home/home.html",
        {
            "questions": questions,
        },
    )
