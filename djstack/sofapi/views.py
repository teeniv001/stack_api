from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import questions
from .serializer import questionserializer

import requests
from bs4 import BeautifulSoup
import json

# Create your views here.

def index(request):
    return HttpResponse("Success")

class questionsAPI(viewsets.ModelViewSet):
    #querySet is from where the data will come
    queryset = questions.objects.all()
    serializer_class = questionserializer


def latest(request):
    try:
        res = requests.get("https://stackoverflow.com/questions")
        soup = BeautifulSoup(res.text,"html.parser")
        Questions = soup.select(".question-summary")
        for que in Questions:
            q = que.select_one(".question-hyperlink").getText()
            vote_count = que.select_one(".vote-count-post").getText()
            views = que.select_one(".views").attrs['title']

            question = questions()
            # .objects are coming from models
            question.questions = q
            question.vote_count = vote_count
            question.views = views

            question.save()
        return HttpResponse("latest data fetched")
    except :
        return HttpResponse("failed")


    
