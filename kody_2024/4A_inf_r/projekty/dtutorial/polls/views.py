from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import F
from .models import Question, Choice
from django.urls import reverse, reverse_lazy
from django.views import generic

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    pytanie = get_object_or_404(Question, pk=question_id)
    try:
        odp = pytanie.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html",
                      {"question": pytanie, "error_message": "Nie wybrałeś odpowiedzi!"}
                      )

    odp.votes = F("votes") + 1
    odp.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))

class QuestionDelete(generic.DeleteView):
    model = Question
    template_name = "polls/delete.html"
    success_url = reverse_lazy("polls:index")

# def index(request):
#     latest_question = Question.objects.order_by("-pub_date")[:5]
#     print(latest_question)
#     context = {
#         "latest_question": latest_question,
#     }
#     return render(request, "polls/index.html", context)

# def detail(request, pytanie_id):
#     try:
#         pytanie = get_object_or_404(Question, pk=pytanie_id)
#     except Question.DoesNotExist:
#         raise Http404("Pytanie nie istnieje!")
#     return render(request, "polls/detail.html", {"pytanie": pytanie})

# def results(request, question_id):
#     pytanie = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"pytanie": pytanie})

# def info(request):
#     return HttpResponse("<h1>Informacje</h1><p>To bardzo ważne informacje</p>")
