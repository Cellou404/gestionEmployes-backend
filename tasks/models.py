from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField( blank=True)
    complete = models.BooleanField(verbose_name=_('complete'), default=False)
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.title}-{timezone.localdate(timezone.now())}")

        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

