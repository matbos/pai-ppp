import os

from django.db import models
from django.core.urlresolvers import reverse


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    superCategory = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('hurtownia.views.category', args=[self.id])


class Item(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    lastModification = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, null=True, blank=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('item', args=[self])

        # class Photo(models.Model):
        # profile_image = ImageField(upload_to=get_image_path, blank=True, null=True)


