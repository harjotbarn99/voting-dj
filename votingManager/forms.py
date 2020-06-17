from django import forms
from getSeededTeam.models import Candidate


class AddVoteCodes(forms.Form):
    number = forms.NumberInput()



class DeleteVoteCodes(forms.Form):
    code = forms.CharField(max_length=20)





