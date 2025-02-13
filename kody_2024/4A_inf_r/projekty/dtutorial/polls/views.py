from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import F
from .models import Pytanie, Odpowiedz
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.forms.models import inlineformset_factory


def index(request):
    return render(request, "polls/index.html")

class PytanieLista(generic.ListView):
    def get_queryset(self):
        """Return the last five published questions."""
        return Pytanie.objects.order_by("-data_pub")[:5]

class DetailView(generic.DetailView):
    model = Pytanie
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Pytanie
    template_name = "polls/results.html"

def vote(request, question_id):
    pytanie = get_object_or_404(Pytanie, pk=question_id)
    try:
        odp = pytanie.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Odpowiedz.DoesNotExist):
        return render(request, "polls/detail.html",
                      {"pytanie": pytanie, "error_message": "Nie wybrałeś odpowiedzi!"}
                      )

    odp.glosy = F("glosy") + 1
    odp.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))

class PytanieDelete(generic.DeleteView):
    model = Pytanie
    template_name = "polls/delete.html"
    success_url = reverse_lazy("polls:index")


@method_decorator(login_required, 'dispatch')
class PytanieCreate(generic.CreateView):
    model = Pytanie
    fields = ["tekst_pytania"]
    success_url = reverse_lazy('polls:index')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

@method_decorator(login_required, 'dispatch')
class OdpowiedzCreate(generic.CreateView):
    model = Odpowiedz
    
# def index(request):
#     latest_question = Pytanie.objects.order_by("-data_pub")[:5]
#     print(latest_question)
#     context = {
#         "latest_question": latest_question,
#     }
#     return render(request, "polls/index.html", context)

# def detail(request, pytanie_id):
#     try:
#         pytanie = get_object_or_404(Pytanie, pk=pytanie_id)
#     except Pytanie.DoesNotExist:
#         raise Http404("Pytanie nie istnieje!")
#     return render(request, "polls/detail.html", {"pytanie": pytanie})

# def results(request, question_id):
#     pytanie = get_object_or_404(Pytanie, pk=question_id)
#     return render(request, "polls/results.html", {"pytanie": pytanie})

# def info(request):
#     return HttpResponse("<h1>Informacje</h1><p>To bardzo ważne informacje</p>")
