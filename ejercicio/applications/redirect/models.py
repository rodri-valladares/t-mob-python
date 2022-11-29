from django.db import models
from datetime import datetime 
# Create your models here.
class Redirect(models.Model):
    key = models.CharField('Key', max_length=50, unique=True)
    url = models.URLField(null=True, blank=True)
    active = models.BooleanField('Active',default=False)
    updated_at = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.key + '-' + self.active