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

    AUDIENCE = (
        ('B', 'Beginners'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
        ('E', 'Everybody'),
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='proposals')
    title = models.CharField(max_length=250, blank=False, null=False, help_text='a short title of your talk')
    slug = models.SlugField(max_length=255, blank=False, null=False)
    category = models.CharField(max_length=2, choices=CATEGORIES, blank=False, null=False, help_text='Where does your talk fit in?')
    abstract = models.TextField(blank=False, null=False, help_text='a summary on why this talk is neccessary')
    description = models.TextField(blank=False, null=False, help_text='content of your talk as to be shown to the public')
    pre_requesite = models.TextField(blank=True, null=True, help_text='what are the pre-requisites for this talk?')
    audience = models.CharField(max_length=2, choices=AUDIENCE, default='E', help_text='Who are your target audience?')
    about_author = models.TextField(blank=False, null=False, help_text='Let us know a little more about you')
    website = models.URLField(blank=True, null=True, help_text='have a link to your personal website/blog?')
    profile_picture = models.ImageField(upload_to = 'pic_folder/', help_text='a nice image of you')
    submitted = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
    	self.slug = slugify(self.title)
    	super(Proposal, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


