from django.shortcuts import render, redirect #, get_object_or_404
# from django.views.generic import (
#     ListView,
#     DetailView,
#     CreateView,
#     UpdateView,
#     DeleteView
# )
from .models import VoteCode
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# from .forms import AddVoteCodes, DeleteVoteCodes
from .votingHelper import addVoteCodes, deleteVoteCode, checkCode, castVote, getVotingStatus, changeVotingStat
from django.contrib import messages
# from .forms import CastVoteForm, GettingCandidates
from getSeededTeam.models import Candidate
# Create your views here.


@login_required
def home_VM(request):
    allVoteCodes = VoteCode.objects.all()
    length = len(allVoteCodes)
    context = {"voteCodes": allVoteCodes, "title": "Voting Manager Home - Get Seeded", "vStat": getVotingStatus(), "length": length}
    return render(request, "voteManager/home_VM.html",context)


@login_required
def addVoteCodes_VM(request):
    num = request.POST.get("number")
    addVoteCodes(num)
    messages.success(request, f'{num} Vote Codes Added')
    return redirect('home-VM')


@login_required
def deleteVoteCode_VM(request):
    code = request.POST.get("code")
    status = checkCode(code)
    if status == "failed":
        messages.error(request, f"{code} is not a valid Vote Code")
        return redirect('home-VM')
    elif status == "success":
        deleteVoteCode(code)
        messages.success(request, f'Vote Codes deleted')
        return redirect('home-VM')
    else:
        messages.error(request, f" there's a bug while deleting code")
        return redirect('home-VM')


@login_required
def deleteAllVoteCodesConfirm_VM(request):
    return render(request, "voteManager/deleteAllVoteCodesConfirm_VM.html", {"title": "Confirm Deleting All Vote Codes"})


@login_required
def deleteAllVoteCodes_VM(request):
    VoteCode.objects.all().delete()
    messages.success(request, f' All Vote Codes Deleted')
    return redirect('home-VM')


@login_required
def changeVotingStat_VM(request):
    message = changeVotingStat()
    return redirect('home-VM')



def votingPage_VM(request):
    if request.method == "GET":
        techList = Candidate.objects.filter(category="Technology")
        genList = Candidate.objects.filter(category="General")
        socialList = Candidate.objects.filter(category="Social")
        context = {
            "techs": techList,
            "gens" : genList,
            "socs" : socialList,
            "title" : "Voting Page - Get Seeded",
            "vStat": getVotingStatus()
        }
        return render(request, "votingPage/votingPage_Voting.html", context)
    elif request.method == "POST":
        data = request.POST
        message = castVote(data)
        techList = Candidate.objects.filter(category="Technology")
        genList = Candidate.objects.filter(category="General")
        socialList = Candidate.objects.filter(category="Social")
        context = {
            "techs": techList,
            "gens": genList,
            "socs": socialList,
            "title": "Voting Page - Get Seeded",
            "vStat": getVotingStatus()
        }
        messages.success(request, message)
        return render(request, "votingPage/votingPage_Voting.html", context)
    context = {
        "title" : "Voting Page - Get Seeded"
    }
    messages.error(request, "problem during loading page")
    return render(request, "votingPage/votingPage_Voting.html", context)





