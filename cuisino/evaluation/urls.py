from django.urls import path
from evaluation import views

urlpatterns = [
    #http://localhost/evaluation - evaluation main page
    path('', views.main),
    #http://localhost/evaluation evaluation -  save evaluation
    path('save_evaluation', views.save_evaluation),
    #http://localhost/survey/save_evaluation - showing evaluation result
    path('show_result', views.show_result),
]