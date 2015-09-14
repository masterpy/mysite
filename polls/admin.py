from django.contrib import admin
from .models import Question,Choice

# Register your models here.


class ChoiceInline(admin.TabularInline):#左右结构，StackedInline为上下结构
    model = Choice
    extra = 3                           #额外显示3个Choice选项


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['question_text']}),
        ('Date information',{'fields':['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    #以列表的方式显示Question
    list_filter = ['pub_date']#添加过滤器
    search_fields = ['question_text']#添加搜索功能

admin.site.register(Question,QuestionAdmin)#告诉管理站点Question对象要有一个管理界面
