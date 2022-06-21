from django.shortcuts import render


# Create your views here.


def index_view(request):
    if request.method == "POST":
        return render(request, "index.html")


def game_number(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.POST.getlist('text') == 'numbers':
        result_return = int(request.POST.get('numbers'))
        context = {
            'result': f"Result: {request.POST.get('numbers')}"
        }
        print(context)

    return render(request, "index.html", context)

def validation(request):
    secret_number = [1, 2, 3, 4]
    try:
        result_return = [int(i) for i in "numbers"]
        if len(result_return) != 4:
            return "The amount of integers ahould egual to 4"
        if len(result_return) != len(set(result_return)):
            return "The value should be inig"
        for i in result_return:
            if i > 9 or i < 1:
                return "Numbers must be greater then 1 and less then 10"
    except:
        return "The value should be integers"

def get_result(request):
    bulls = 0
    cows = 0
    for i in range(len(request.result_return)):
        if request.result_return[i] == request.secret_number[i]:
            bulls += 1
        elif request.result_return[i] in request.secret_number:
            cows += 1

    if bulls == 4:
        return "Winner"
    elif bulls or cows:
        return f"You got {bulls} bulls and {cows} cows"
    else:
        return "No identical number"

