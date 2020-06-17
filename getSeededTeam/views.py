from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Candidate
from votingManager.votingHelper import changeVotingStat
# Create your views here.

@login_required
def home_getSeededTeam(request):
    map ={
        'title': "Home Get seeded Team"
    }
    return render(request, "getSeededTeam/home_getSeededTeam.html",map)

@login_required
def results_getSeededTeam(request):
    changeVotingStat()
    techList = Candidate.objects.filter(category="Technology").order_by("-votes")
    genList = Candidate.objects.filter(category="General").order_by("-votes")
    socialList = Candidate.objects.filter(category="Social").order_by("-votes")
    context = {
        "techs": techList,
        "gens" : genList,
        "socs" : socialList,
        "title" : "Voting Page - Get Seeded",
    }
    return render(request, "getSeededTeam/resultsPage_getSeeded.html", context)

def register_getSeededTeam(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! with the username {username}, you are now able to log in')
            return redirect('login-getSeededTeam')
    else:
        form = UserRegisterForm()
    return render(request, 'getSeededTeam/gstAuth/register_getSeededTeam.html', {'form': form, "title": "Register - Get Seeded Team"})


class AddCandidateView(LoginRequiredMixin, CreateView):
    template_name = "getSeededTeam/addCandidate_getSeededTeam.html"
    model = Candidate
    fields = ["name", 'category' ,'venture','details']
    success_url = "/getseededteam/candidates"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = "Add Candidate - Get Seeded Team"
        context["title"] = title
        return context



class CandidatesListView(LoginRequiredMixin, ListView ):
    model = Candidate
    template_name = "getSeededTeam/candidatesList_getSeededTeam.html"
    context_object_name = 'candidates'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = "Candidates List - Get Seeded Team"
        context["title"] = title
        return context



class CandidateDetailView(LoginRequiredMixin, DetailView):
    model = Candidate
    template_name = "getSeededTeam/candidateDetail_getSeededTeam.html"
    # context_object_name = 'candidates'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = "Candidate Details - Get Seeded Team"
        context["title"] = title
        return context




class CandidateUpdateView(LoginRequiredMixin,UpdateView):
    model = Candidate
    template_name = "getSeededTeam/candidateUpdate_getSeededTeam.html"
    fields = ["name", 'category', 'image' ,'venture','details']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = "Update Candidates - Get Seeded Team"
        context["title"] = title
        return context




class CandidateDeleteView(LoginRequiredMixin, DeleteView):
    model = Candidate
    template_name = "getSeededTeam/candidateDelete_getSeededTeam.html"
    success_url = "/getseededteam/candidates"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = "Delete Candidates - Get Seeded Team"
        context["title"] = title
        return context



@login_required
def deleteAllCandidatesConfirm_getSeededTeam(request):
    map={"title":"Delete all - Get Seeded Team "}
    return render(request,"getSeededTeam/deleteAllCandidatesConfirm_getSeededTeam.html")


@login_required
def deleteAllCandidates_Request(request):
    Candidate.objects.all().delete()
    messages.success(request, f'All Candidates Deleted')
    return redirect('candidatesList-getSeededTeam')

@login_required
def clearVotes_GST(request):
    all = Candidate.objects.all()
    for cand in all:
        cand(votes=0).save()
    messages.success(request, f'Votes cleared')
    return redirect('candidatesList-getSeededTeam')


