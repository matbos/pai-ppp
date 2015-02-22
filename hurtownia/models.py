import os

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from ProjektPPPPAI import settings


def get_image_path(instance, filename):
    return os.path.join(settings.BASE_DIR, str(instance.id), filename)


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    superCategory = models.ForeignKey('self', null=True, blank=True, default=None)
    visible = models.BooleanField(default=True)
    slug = models.SlugField()

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        slug = ""
        super_cat = self.superCategory
        slug_list = []

        while super_cat:
            slug_list.append(super_cat.slug)
            super_cat = super_cat.superCategory

        if slug_list:
            slug_list.reverse()
            for sl in slug_list:
                slug += sl + "-"
        slug += self.title
        return reverse('hurtownia.views.category_view', args=[self.id, slug])


class Item(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    lastModification = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    creator = models.ForeignKey(User, null=True, unique=False, related_name="creator_of")
    slug = models.SlugField(max_length=50)
    price = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('hurtownia.views.item_view', args=[self.slug])


class Photo(models.Model):
    image = models.ImageField()
    uploaded = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.image.name

    def get_absolute_url(self):
        return os.path.join(settings.BASE_DIR, self.image.url)


class Indent(models.Model):
    user = models.ForeignKey(User, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    lastModification = models.DateTimeField(auto_now_add=True)


class IndentPosition(models.Model):
    item = models.ForeignKey(Item, blank=False)
    quantity = models.PositiveIntegerField(blank=False, default=1)
    indent = models.ForeignKey(Indent, blank=False)


class IndentComment(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(User, blank=False)
    indent = models.ForeignKey(Indent, blank=False)

