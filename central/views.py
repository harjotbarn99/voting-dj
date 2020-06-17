from django.shortcuts import render, redirect #, get_object_or_404
# from django.views.generic import (
#     ListView,
#     DetailView,
#     CreateView,
#     UpdateView,
#     DeleteView
# )
# from votingManager.models import VoteCode
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
# from .forms import AddVoteCodes, DeleteVoteCodes
# from votingManager.votingHelper import addVoteCodes, deleteVoteCode, checkCode
# from django.contrib import messages
# from .forms import CastVoteForm, GettingCandidates
# from getSeededTeam.models import Candidate
# Create your views here.

# Create your views here.

def homepage_central(request):
    map = {
        "title": "HomePage - Central"
    }
    return render(request,"central/home_central.html",map)

