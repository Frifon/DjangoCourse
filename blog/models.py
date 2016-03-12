# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

import constants
from .utils import models_langs

# Create your models here.


class AuthorName(models.Model):
    ru = models.CharField(max_length=constants.MAXLEN_AUTHOR_NAME)
    en = models.CharField(max_length=constants.MAXLEN_AUTHOR_NAME)

    def __unicode__(self):
        return models_langs(self)[constants.DEFAULT_LANG]


class MaterialMarkName(models.Model):
    ru = models.CharField(max_length=constants.MAXLEN_MATERIAL_MARK_NAME)
    en = models.CharField(max_length=constants.MAXLEN_MATERIAL_MARK_NAME)

    def __unicode__(self):
        return models_langs(self)[constants.DEFAULT_LANG]


class MaterialMarkBlockName(models.Model):
    ru = models.CharField(max_length=constants.MAXLEN_MATERIAL_MARK_BLOCK_NAME)
    en = models.CharField(max_length=constants.MAXLEN_MATERIAL_MARK_BLOCK_NAME)

    def __unicode__(self):
        return models_langs(self)[constants.DEFAULT_LANG]


class MaterialMarkData(models.Model):
    ru = models.CharField(max_length=constants.MAXLEN_MATERIAL_MARK_DATA)
    en = models.CharField(max_length=constants.MAXLEN_MATERIAL_MARK_DATA)

    def __unicode__(self):
        return models_langs(self)[constants.DEFAULT_LANG]


class MaterialMarkBlock(models.Model):
    name = models.ForeignKey(
                             'MaterialMarkBlockName',
                             on_delete=models.SET_NULL,
                             null=True
                             )

    def __unicode__(self):
        return str(self.name)


class MaterialMark(models.Model):
    material = models.ForeignKey(
                                 'Material',
                                 on_delete=models.SET_NULL,
                                 null=True
                                 )

    name = models.ForeignKey(
                             'MaterialMarkName',
                             on_delete=models.SET_NULL,
                             null=True
                             )

    block = models.ForeignKey(
                              'MaterialMarkBlock',
                              on_delete=models.SET_NULL,
                              null=True
                              )

    data = models.ForeignKey(
                              'MaterialMarkData',
                              on_delete=models.SET_NULL,
                              null=True
                              )

    mark_type = models.IntegerField()
    permissions = models.IntegerField()

    def __unicode__(self):
        return '{0}: {1}'.format(self.name, self.data)


class Author(models.Model):
    name = models.ForeignKey(AuthorName, on_delete=models.SET_NULL, null=True)

    def __unicode__(self):
        return "[{0}] {1}".format(str(self.id), self.name)


class Material(models.Model):
    created_date = models.DateTimeField(default=timezone.now)

    def get_marks(self):
        return MaterialMark.objects.filter(material__id=self.id)

    def __unicode__(self):
        res = "[{0}] ".format(str(self.id))
        res += ", ".join(map(str, self.get_marks()))
        return res

