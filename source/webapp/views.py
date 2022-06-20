from django.shortcuts import render
from urllib.parse import parse_qs


# Create your views here.


def index_view(request):
    if request.method == "POST":
        number_str = parse_qs(request)["numbers"][0].split()
        print(number_str)
    return render(request, "index.html")


def validation(number_str):
    secret_number = [1, 2, 3, 4]
    try:
        numbers = [int(s) for s in number_str]
        if len(numbers) != 4:
            return "The amount of integers ahould egual to 4"
        if len(numbers) != len(set(numbers)):
            return "The value should be inig"
        for i in numbers:
            if i > 9 or i < 1:
                return "Numbers must be greater then 1 and less then 10"
    except:
        return "The value should be integers"

def get_result(request):
    bulls = 0
    cows = 0
    for i in range(len(request.numbers)):
        if request.numbers[i] == request.secret_number[i]:
            bulls += 1
        elif request.numbers[i] in request.secret_number:
            cows += 1

    if bulls == 4:
        return "Winner"
    elif bulls or cows:
        return f"You got {bulls} bulls and {cows} cows"
    else:
        return "No identical number"



def game_number(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.POST.get('numbers'):
        result_return = int(request.POST.get('numbers'))
