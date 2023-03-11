from django.db import models
from datetime import datetime
from django.utils.translation import gettext as _ # For translation purpose
from django.template.defaultfilters import slugify
from django.utils import timezone


# =========================== Employee Model ============================= #

class Employee(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=150) # `_('...')` field name can be translated
    email = models.CharField(verbose_name=_('email'), max_length=150)
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d', blank=True)
    designation = models.CharField(verbose_name=_('designation'), max_length=150)
    bio = models.TextField(
        verbose_name=_('bio'), 
        max_length=500, blank=True, 
        help_text=_('500 characters allowed')
    )
    phone = models.CharField(verbose_name=_('phone'), max_length=20, blank=True)
    address = models.CharField(verbose_name=_('address'), max_length=150, blank=True)
    salary = models.PositiveIntegerField(verbose_name=_('salary'), blank=True)
    date_hired = models.DateTimeField(default=datetime.now, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    
    # This method will fill the slug field so the we don't have to manualy type it
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.name}-{self.designation}-{timezone.localdate(timezone.now())}")

        super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")
