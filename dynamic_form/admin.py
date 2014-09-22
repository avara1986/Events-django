# encoding: utf-8
from django.contrib import admin
from .models import Question, Answer


class DynamicFormMixinBase(object):
    pass


class DynamicFormQuestionerMixin(DynamicFormMixinBase):
    def get_questions(self):
        return Question.objects.filter(questioner=self.id)


class DynamicFormAnswererMixin(DynamicFormMixinBase):
    def get_questions(self):
        return Answer.objects.filter(answerer=self.id)


class QuestionInline(admin.TabularInline):
    model = Question


class AnswerInline(admin.TabularInline):
    model = Answer
    readonly_fields = ('question', 'answer')


class AnswerAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.another_field == 'cant_change_question':
            return self.readonly_fields + ['question']
        return self.readonly_fields


admin.site.register(Question)
admin.site.register(Answer, AnswerAdmin)
