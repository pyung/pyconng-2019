from django import forms
from .models import Proposal


class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        exclude = ('accepted', 'author','slug', 'submitted')
