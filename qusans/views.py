from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import QuestionCreateForm, AnswerCreateForm
from .models import Question, Answer
from django.utils import timezone


def questionAnswer(request):
    questionList = Question.objects.all()

    qform = QuestionCreateForm()
    aform = AnswerCreateForm()
    context = {
        'qform': qform,
        'aform': aform,
        'questionList': questionList,
    }
    return render(request, 'qusans/questionanswer.html', context)

class QuestionCreateView(CreateView):
    template_name = 'qusans/questionanswer.html'
    form_class = QuestionCreateForm
    success_url = reverse_lazy('qusans')
    model = Question

    def form_valid(self, form):
        return super().form_valid(form)

class AnswerCreateView(LoginRequiredMixin, CreateView):
    template_name = 'qusans/questionanswer.html'
    form_class = AnswerCreateForm
    success_url = reverse_lazy('qusans')
    model = Answer

    def form_valid(self, form):
        print("form_valid {}".format(self.kwargs['q_id']))
        #form.instance.doctor = self.request.user
        question= None

        try:
            question = Question.objects.filter(id=self.kwargs['q_id'])
            a = Answer(doctor=self.request.user,quest=question[0],ans=form.cleaned_data['ans'],appreciation=None)
            a.save()
            print(question)
        except Exception:
            print(question)

        #form.instance.quest = Question.objects.get_object_or_404(id=self.kwargs['q_id'])
        return super().form_valid(form)
