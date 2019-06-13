from django.shortcuts import render
from .forms import ProposalForm
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden


class ProposalCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create_proposal.html'
    form_class = ProposalForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ProposalUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'update_proposal.html'
    form_class = ProposalForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.instance.created_by = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        """ Making sure that only authors can update their proposals """
        obj = self.get_object()
        if obj.author != self.request.user:
            return HttpResponseForbidden()
        return super(ProposalUpdateView, self).dispatch(request, *args, **kwargs)
