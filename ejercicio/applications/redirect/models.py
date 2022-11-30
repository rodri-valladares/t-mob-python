from django.core.cache import cache
from django.db import models
from datetime import datetime 
from django.db.models.signals import post_save


class Redirect(models.Model):
    key = models.CharField('Key', max_length=50, unique=True)
    url = models.URLField(null=True, blank=True)
    active = models.BooleanField('Active',default=False)
    updated_at = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.key + ' - Active:' + str(self.active)


def guardar_cache_active(sender, instance, **kwargs):
    #Si active es True se guarda en cache
    if instance.active == True:
        element_active = Redirect.objects.filter(key=instance.key)
        cache.set(instance.key, element_active)

post_save.connect(guardar_cache_active, sender = Redirect)