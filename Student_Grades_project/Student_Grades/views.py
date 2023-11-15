from django.http import HttpResponse
from django.shortcuts import render
import joblib

def HomePage(request):
    return render(request,"HomePage.html")

def results(request):
    
    cls=joblib.load('Grade_model.joblib')
    lis=[]

    lis.append(request.GET['QUIZZES'])
    lis.append(request.GET['PROJECT'])
    lis.append(request.GET['MID-EXAM'])
    lis.append(request.GET['FINAL-EXAM'])

    answer=cls.predict([lis])

    return render(request,"results.html",{'answer':answer})

