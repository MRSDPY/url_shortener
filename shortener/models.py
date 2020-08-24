from django.db import models
from .Generator.generator import unique_generator
from django.conf import settings


class Shortener(models.Manager):
    def all(self, *args, **kwargs):
        all_query = super(Shortener, self).all(*args, **kwargs)
        final_modify = all_query.filter(activate=True)
        return final_modify


class OpenUrls(models.Model):
    origin_url = models.URLField()
    shorted_url = models.CharField(max_length=settings.MAX_SIZE, blank=True, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    activate = models.BooleanField(default=True)
    click = models.PositiveIntegerField(default=0)

    objects = Shortener()

    def save(self, *args, **kwargs):
        if self.shorted_url is None or self.shorted_url is "":
            self.shorted_url = unique_generator(instance=self)
        super(OpenUrls, self).save(*args, **kwargs)
