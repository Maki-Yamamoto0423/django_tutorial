from django.http import HttpResponse

def index(request):
    return HttpResponse("You're looking at polls.")

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")