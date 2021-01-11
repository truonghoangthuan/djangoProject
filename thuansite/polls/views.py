from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
    myName = "Hoang Thuan"
    myGoods = ["phone", "pc", "bike", "money"]
    context = {"name": myName,
               "goods": myGoods}
    return render(request, "polls/index.html", context)

def viewList(request):
    listQuestion = Question.objects.all()
    context = {"questList": listQuestion}
    return render(request, "polls/questionList.html", context)

def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request, "polls/detail_question.html", {"qs": q})