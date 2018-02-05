from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from django.views.decorators.csrf import csrf_exempt

import delta_qa.settings as sett
import json

# import model
from qa.models import CQA

# model pub date need this
from django.utils import timezone

@csrf_exempt
def valid(request):
    if request.method == 'POST':

        valid_code = request.POST.get('valid_code')
        cqa_id = request.POST.get('cqa_id')

        print("cqa_id", cqa_id)

        q = CQA.objects.get(pk=cqa_id)
        q.valid = valid_code
        q.save()
        print(q)
        return HttpResponse("hello, valid")

    else:
        return HttpResponse("hello, you should use post")

@csrf_exempt
def index(request):
    if request.method == 'POST':

        context = request.POST.get('context')
        question = request.POST.get('question')
    #
        contexts = [context]
        questions = [question]
        Y_str, Y_end = sett.qaModel.infer(contexts, questions, getIndex=True)
        answers = [contexts[i][Y_str[i]:Y_end[i]] for i in range(len(contexts))]

        # Update query history
        # __todo__
        pub_date = pub_date=timezone.now()
        context_text = context
        question_text = question
        answer_start = Y_str[0]
        answer_end = Y_end[0]
        answer_text = answers[0]
        valid = 0
        cqa = CQA()
        cqa.pub_date = pub_date
        cqa.context_text = context_text
        cqa.question_text = question_text
        cqa.answer_start = answer_start
        cqa.answer_end = answer_end
        cqa.answer_text = answer_text
        cqa.valid = valid

        cqa.save()

        return HttpResponse(json.dumps({'start_idx':int(Y_str[0]), 'end_idx':int(Y_end[0]), 'cqa_id':cqa.id}))

    else:
        return HttpResponse("hello, you should use post")
