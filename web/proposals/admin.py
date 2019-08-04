from django.contrib import admin
from .models import Proposal

# Register your models here.

class ProposalAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Proposal, ProposalAdmin)