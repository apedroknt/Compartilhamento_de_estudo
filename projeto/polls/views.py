from django.http import HttpResponse


def index(request):
    return HttpResponse("Rafael um aumento por favor")