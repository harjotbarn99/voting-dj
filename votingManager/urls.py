"""get_seeded URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home_VM, deleteAllVoteCodesConfirm_VM, deleteAllVoteCodes_VM, addVoteCodes_VM, deleteVoteCode_VM, changeVotingStat_VM


urlpatterns = [
    path("",home_VM,name="home-VM"),
    path("deleteAllVoteCodesConfirm",deleteAllVoteCodesConfirm_VM,name="deleteAllVoteCodesConfirm-VM"),
    path("deleteAllVoteCodesConfirm/delete",deleteAllVoteCodes_VM,name="deleteAllVoteCodes-VM"),
    path("addVoteCodes/",addVoteCodes_VM,name="addVoteCodes-VM"),
    path("deleteVoteCode/",deleteVoteCode_VM,name="deleteVoteCode-VM"),
    path("changeVotingStat/",changeVotingStat_VM,name="changeVotingStatus-VM"),


]

