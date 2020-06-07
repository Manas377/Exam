from django.shortcuts import render
from django.forms import formset_factory

# Create your views here.


from django.shortcuts import render, redirect
from django.views.generic import View, FormView
from exam.models import TestSet, Question
from django.forms import modelformset_factory
from forms.forms import TestAnswerForm, AnswerForm, QuestionForm, TestSetForm
from result.models import Answer


class Home (View):
    def get(self, *args, **kwargs):
        return render (self.request, 'home-page.html')


def TestView(request):
    formsetclass = modelformset_factory(Question, QuestionForm, fields={'question', 'choice_1', 'choice_2',
                                                                         'choice_3', 'choice_4', 'marks',
                                                                         'correct_choice'}, extra=0)
    test_set_qs = TestSet.objects.filter(title='A')
    test_set = test_set_qs[0]
    answerformsetclass = modelformset_factory(Answer, AnswerForm, fields='__all__',
                                              extra=test_set.questions.all().count())

    if request.method == 'GET':
        formset = formsetclass(queryset=test_set.questions.all())

        context = {
            'forms': formset,

        }
        return render(request, 'test-page2.html', context)

    else:
        print(request.POST)
        # return True
        # forms = answerformsetclass(request.POST)
        # print(forms.as_ul())
        #
        # if forms.is_valid():
        #     pass
        # else:
        #     print(forms.errors)
        # instances = forms.save(commit=False)
        # for instance in instances:
        #     pass
        #
        return redirect('exam:test')





# class TestView(View):
#     formsetclass = modelformset_factory (Question, QuestionForm, fields={'question', 'choice_1', 'choice_2',
#                                                                          'choice_3', 'choice_4', 'marks',
#                                                                          'correct_choice'}, extra=0)
#     test_set_qs = TestSet.objects.filter(title='A')
#     test_set = test_set_qs[0]
#     answerformsetclass = modelformset_factory(Answer, AnswerForm, fields='__all__',
#                                               extra=test_set.questions.all().count())
#
#     def get(self, *args, **kwargs):
#         formset = self.formsetclass(queryset=self.test_set.questions.all())
#         answerformset = self.answerformsetclass()
#         context = {
#             'forms': formset,
#             'answer_forms': answerformset
#         }
#         return render(self.request, 'test-page1.html', context)
#
#     def post(self, *args, **kwargs):
#         formset = self.answerformsetclass(self.request.POST)
#         if formset.is_valid():
#             pass
#         else:
#             print(formset.errors)
#         instances = formset.save(commit=False)
#         for instance in instances:
#             pass
#
#         return redirect('exam:test')





























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

