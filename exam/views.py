from django.shortcuts import render


# Create your views here.


from django.shortcuts import render, redirect
from django.views.generic import View, FormView
from exam.models import TestSet, Question
from django.forms import modelformset_factory
from forms.forms import TestAnswerForm, AnswerForm, QuestionForm, TestSetForm
from result.models import Answer, AnswerSet


class Home (View):
    def get(self, *args, **kwargs):
        return render(self.request, 'home-page.html')


class TestView(View):
    formset_class = modelformset_factory(Question, QuestionForm, fields={'question', 'choice_1', 'choice_2',
                                                                        'choice_3', 'choice_4', 'marks',
                                                                        'correct_choice'}, extra=0)
    test_set = TestSet.objects.filter(title='A').first()
    answer_formset_class = modelformset_factory(Answer, AnswerForm, fields='__all__',
                                              extra=test_set.questions.all().count())
    num = test_set.questions.all ().count ()
    def get(self, *args, **kwargs):
        formset = self.formset_class(queryset=self.test_set.questions.all())

        context = {
            'forms': formset,
            'num': self.num

        }
        return render(self.request, 'test-page.html', context)

    def post(self, *args, **kwargs):
        formset = self.formset_class(self.request.POST)
        answer_formset = self.answer_formset_class()
        answerset, created = AnswerSet.objects.get_or_create(title='A')
        if formset.is_valid():
            print("form is valid")

            for form, answerform in zip(formset, answer_formset):
                question = form.cleaned_data['question']
                answer = form.cleaned_data['answered']
                question_obj = Question.objects.filter(question=question).first()
                answer_obj = Answer(question=question_obj, answered=answer)
                answer_obj.save()
                answerset.answer.add(answer_obj)
                answerset.save()




        else:
            for form in formset:
                print(form.errors)

        return redirect('exam:test')























# class TestView (View):
#     test_query_set = TestSet.objects.filter(title='A').first()  # Change to "User's Assigned Set" After applying user authentication also change it to get object or 404
#     extra = test_query_set.questions.all().count()
#
#     # TestAnswerFormSet = formset_factory(TestAnswerForm, extra=extra, validate_min=True)
#
#     def get(self, *args, **kwargs):
#         # test_set = test_query_set[0]
#         questions = self.test_query_set.questions.all()
#         form = AnswerForm()
#         form2 = AnswerForm()
#         # formset = self.TestAnswerFormSet()
#         context = {
#             'object_list': questions,
#             'form': form,
#             'form2': form2
#
#         }
#         return render(self.request, 'test-page.html', context)
#
#     # have to take data from multiple SIMILAR FORMS
#     # Take only SELECTED DATA which will be stored in Result.Answer model
#     # Then a signal will be sent by answer model after saving to Result set model
#
#     def post(self, *args, **kwargs):
#
#         forms = [TestAnswerForm(self.request.POST, prefix=i) for i in range(self.test_query_set.questions.all().count())]
#         if 2 != 3: # all(form.is_valid() for form in forms):
#             for form in forms:
#                 print([form['question']])
#                 print([form['answer']])
#
#             print(self.request.POST)
#
#         # formset = self.TestAnswerFormSet(self.request.POST)
#         # if formset.is_valid():
#         #     print("Form is valid")
#
#         # else:
#         #     print("form data invalid")
#         #     for form in forms:
#         #         print(form.errors)
#         return redirect('exam:test')

