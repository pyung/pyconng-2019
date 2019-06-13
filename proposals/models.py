from django.db import models
from django.conf import settings
from django.utils import timezone
from django.template.defaultfilters import slugify


# Create your models here.

class Proposal(models.Model):

    CATEGORIES = (
        ('TT', 'Tutorial'),
        ('ST', 'Short Talk'),
        ('LT', 'Long Talk'),
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, blank=False, null=False)
    slug = models.SlugField(max_length=255, blank=False, null=False)
    category = models.CharField(max_length=2, choices=CATEGORIES, blank=False, null=False)
    abstract = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    pre_requesite = models.TextField(blank=False, null=False)
    about_author = models.TextField(blank=False, null=False)
    website = models.URLField()
    submitted = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
    	self.slug = slugify(self.title)
    	super(Proposal, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


