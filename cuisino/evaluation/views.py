from django.shortcuts import render
from evaluation.models import Evaluation, Answer



def main(request):
    #showing record status field is y in order by survey_idx
    #Choose only first record from [0]list
    evaluation=Evaluation.objects.filter(status='y').order_by(
        '-evalution_idx')[0]
    # evalutaion/templates/survey/main.html 페이지로 이동
    return render(request, 'evaluation/main.html',
                  {'evaluation':evaluation})

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def save_evaluation(request):
    row=Answer(evalution_idx=request.POST['evaluation_idx'],
               num=request.POST['num'])
    row.save()
    return render(request, 'survey/success.html')






def show_result(request):
    idx=request.GET['evaluation_idx']#question number
    ans=Evaluation.objects.get(evaluation_idx=idx)#Choose record correspond question number
    answer=[ans.ans1, ans.ans2, ans.ans3 ]#question content

    #function calling sql command
    evaluationList=Evaluation.objects.raw('''
select evaluation_idx, num, count(num) sum_num,
  round((select count(*) from evaluation_answer
    where evaluation_idx=a.evaluation_idx and num = a.num)*100.0 /
         (select count(*) from evaluation_answer
          where evaluation_idx=a.evaluation_idx),1) rate
from evaluation_answer a
where evaluation_idx = %s
group by evaluation_idx, num
order by num
    ''', idx) #deliver idx value to %s
    evaluationList=zip(evaluationList, answer) #combine with same index
    #Move to result page and showing
    return render(request, 'evaluation/result.html', {'evaluationList':evaluationList})


