from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from star.models import Star


def main(request):
    return render(request, 'star/main.html')


@csrf_exempt
def one_star():
    pass


@csrf_exempt
def two_star():
    pass



@csrf_exempt
def three_star():
    pass


@csrf_exempt
def four_star():
    pass


@csrf_exempt
def five_star():
    pass