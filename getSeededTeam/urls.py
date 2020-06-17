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

from django.urls import path
from django.conf import settings
from .views import register_getSeededTeam, AddCandidateView, CandidatesListView, CandidateUpdateView,\
    CandidateDetailView, CandidateDeleteView, deleteAllCandidates_Request,  home_getSeededTeam, \
    deleteAllCandidatesConfirm_getSeededTeam, results_getSeededTeam, clearVotes_GST
from django.contrib.auth import views as auth_views

# app_name = "getSeededTeam"

urlpatterns = [
    path("",home_getSeededTeam, name="home-getSeededTeam"),
    path("candidates/",CandidatesListView.as_view(), name="candidatesList-getSeededTeam"),
    path("candidates/results/", results_getSeededTeam, name="results-getSeededTeam"),
    path('candidates/addCandidate/',AddCandidateView.as_view(), name="addCandidate-getSeededTeam" ),
    path('candidates/<int:pk>/',CandidateDetailView.as_view(), name="candidateDetail-getSeededTeam" ),
    path('candidates/<int:pk>/update/',CandidateUpdateView.as_view(), name="candidateUpdate-getSeededTeam" ),
    path('candidates/<int:pk>/delete/',CandidateDeleteView.as_view(), name="candidateDelete-getSeededTeam" ),
    path('candidates/deleteAllCandidatesConfirm/',deleteAllCandidatesConfirm_getSeededTeam, name ="deleteAllCandidatesConfirm-getSeededTeam"),
    path('candidates/deleteAllCandidatesConfirm/delete',deleteAllCandidates_Request, name ="deleteAllCandidates-getSeededTeam"),
    path("candidates/clearVotes/",clearVotes_GST , name="clearVotes-getSeededTeam"),


    path('register/', register_getSeededTeam, name='register-getSeededTeam'),
    path('login/', auth_views.LoginView.as_view(template_name='getSeededTeam/gstAuth/login_getSeededTeam.html'), name='login-getSeededTeam'),
    path('logout/', auth_views.LogoutView.as_view(template_name='getSeededTeam/gstAuth/logout_getSeededTeam.html'), name='logout-getSeededTeam'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='getSeededTeam/gstAuth/passwordReset_getSeededTeam.html'), name='passwordReset-getSeededTeam'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='getSeededTeam/gstAuth/passwordResetDone_getSeededTeam.html'), name='passwordResetDone-getSeededTeam'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='getSeededTeam/gstAuth/passwordResetConfirm_getSeededTeam.html'), name='passwordResetConfirm-getSeededTeam'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='getSeededTeam/gstAuth/passwordResetComplete_getSeededTeam.html'), name='passwordResetComplete-getSeededTeam'),



]

