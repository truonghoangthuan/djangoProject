from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    myName = "Hoang Thuan"
    myGoods = ["phone", "pc", "bike", "money"]
    context = {"name": myName,
               "goods": myGoods}
    return render(request, "polls/index.html", context)