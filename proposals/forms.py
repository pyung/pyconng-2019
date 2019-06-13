from django.forms import ModelForm
from .models import Proposal


class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        exclude = ('accepted', 'author',)
