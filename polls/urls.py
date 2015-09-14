__author__ = 'CBBking'
from . import views
from django.conf.urls import url

#应用内部的urls文件

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<question_id>[0-9]+)/result/$',views.results,name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='votc'),
]