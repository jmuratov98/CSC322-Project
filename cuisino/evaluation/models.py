from django.db import models

#compiment and complain
class Evaluation(models.Model):
    #Index
    survey_idx = models.AutoField(primary_key=True)
    #Chef(food), delivery
    question = models.TextField(null=False)
    #ans1 = complain / ans2 = compliment /ans = not answer
    ans1 = models.TextField(null=True)
    ans2 = models.TextField(null=True)
    ans3 = models.TextField(null=True)
    #evaluation condition
    status = models.CharField(max_length=1, default="y")


# Answer part
class Answer(models.Model):
    #answer Id(auto increment)
    answer_idx = models.AutoField(primary_key=True)
    #answering id (connecting Evaluation's idx field and foreign key)
    survey_idx = models.IntegerField()
    #Answering number
    num=models.IntegerField()