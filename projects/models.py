from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model

User = get_user_model()


# ======================== Project Model =========================== #
class Project(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=200)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description = models.TextField(verbose_name=_('description'), blank=True)
    complete = models.BooleanField(verbose_name=_('complete'), default=False)
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.title}-{timezone.localdate(timezone.now())}")

        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created']
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
    

# ======================== Project Task Model =========================== #
class ProjectTask(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # A project can have multiple tasks
    task_name = models.CharField(verbose_name=_('task name'), max_length=200)
    description = models.TextField(verbose_name=_('description'), max_length=500, help_text=_('500 characters allowed'))
    complete = models.BooleanField(verbose_name=_('complete'), default=False)
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.task_name}-{timezone.localdate(timezone.now())}")

        super(ProjectTask, self).save(*args, **kwargs)

    def __str__(self):
        return self.task_name
    
    class Meta:
        ordering = ['created']
        verbose_name = _('Project Task')
        verbose_name_plural = _('Project Tasks')