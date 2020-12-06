from django.shortcuts import render
from survey.models import Survey



def main(request):
    return render(request, 'survey/main.html')


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def increase_employeesCompliment(request):

    employeesCompliment = +1

    employeesCompliment.save()
    return render(request, 'survey.html')

@csrf_exempt
def increase_employeesComplain(request):
    employeesComplain = +1

    employeesComplain.save()
    return render(request, 'survey.html')










