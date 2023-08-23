from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import Question   #Choice
from django.utils import timezone

from .utils import DataMixin


class IndexView(DataMixin, ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Опросы')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")


class DetailPollView(DataMixin, DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Опрос')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(DataMixin, DetailView):
    model = Question
    template_name = "polls/results.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Результаты')
        return dict(list(context.items()) + list(c_def.items()))


# class AddChoice(LoginRequiredMixin, DataMixin, CreateView):
#     form_class = AddChoiceForm
#     template_name = 'polls/add_choice.html'
#     success_url = reverse_lazy('home')
#     login_url = reverse_lazy('home')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Добавление варианта ответа")
#         return dict(list(context.items()) + list(c_def.items()))


class AddQuest(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddQuestForm
    template_name = 'polls/add_quest.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление опроса")
        return dict(list(context.items()) + list(c_def.items()))

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in latest_question_list])
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)
#
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            question.option_one_count += 1
        elif selected_option == 'option2':
            question.option_two_count += 1
        elif selected_option == 'option3':
            question.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form option')

        question.save()
        return redirect('results', question.id)
        # return HttpResponseRedirect('results', question_id)




    # question = get_object_or_404(Question, pk=question_id)
    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST["choice"])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(
    #         request,
    #         "polls/detail.html",
    #         {
    #             "question": question,
    #             "error_message": "You didn't select a choice.",
    #         },
    #     )
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    #     return HttpResponseRedirect(reverse("results", args=(question.id,)))
