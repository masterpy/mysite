from django.shortcuts import render

# Create your views here.

#创建视图

from django.http import HttpResponse,Http404
from .models import Question
from django.template import RequestContext,loader
from django.shortcuts import render,get_object_or_404

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = RequestContext(request,{
#         'latest_question_list':latest_question_list,
#     })
#     return HttpResponse(template.render(context))
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {'latest_question_list':latest_question_list,}
    return render(request,'polls/index.html',context)

# def detail(request,question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise  Http404('该问题不存在')
#     return render(request,'polls/detail.html',{'question':question})

def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    html = '你正在看的是第%s个问题的内容'%question_id
    return HttpResponse(html)
def vote(request,question_id):
    html = '你正在向第%s个问题投票'%question_id
    return HttpResponse(html)
