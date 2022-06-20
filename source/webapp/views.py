from django.shortcuts import render
from urllib.parse import parse_qs


# Create your views here.


def index_view(request):
    if request.method == "POST":
        number_str = parse_qs(request)["numbers"][0].split()
        print(number_str)
    return render(request, "index.html")


def validation(number_str):
    try:
        numbers = [int(s) for s in number_str]
        if len (numbers) !=4:
            return "The amount of integers ahould egual to 4"
        if len(numbers) !=len(set(numbers)):
            return "The value should be inig"
        for i in numbers:
            if i > 9 or i < 1:
                return "Numbers must be greater then 1 and less then 10"

    except:
        return "The value should be integers"


def game_number(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.POST.get('numbers'):
        result_return = int(request.POST.get('numbers'))
