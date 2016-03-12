from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

import constants

# Create your models here.


class Material(models.Model):
    created_date = models.DateTimeField(default=timezone.now)


class AuthorName(models.Model):
    ru = models.CharField(max_length=constants.MAXLEN_AUTHOR_NAME)
    en = models.CharField(max_length=constants.MAXLEN_AUTHOR_NAME)


class MaterialMarkName(models.Model):
    ru = models.CharField(max_length=constants.MAXLEN_MATERIAL_MARK_NAME)
    en = models.CharField(max_length=constants.MAXLEN_MATERIAL_MARK_NAME)


class MaterialMarkBlockName(models.Model):
    ru = models.CharField(max_length=constants.MAXLEN_MATERIAL_MARK_BLOCK_NAME)
    en = models.CharField(max_length=constants.MAXLEN_MATERIAL_MARK_BLOCK_NAME)


class MaterialMarkBlock(models.Model):
    name = models.ForeignKey(
                             MaterialMarkBlockName,
                             on_delete=models.SET_NULL,
                             null=True
                             )


class MaterialMark(models.Model):
    material = models.ForeignKey(
                                 Material,
                                 on_delete=models.SET_NULL,
                                 null=True
                                 )

    name = models.ForeignKey(
                             MaterialMarkName,
                             on_delete=models.SET_NULL,
                             null=True
                             )

    block = models.ForeignKey(
                              MaterialMarkBlock,
                              on_delete=models.SET_NULL,
                              null=True
                              )

    data = models.CharField(max_length=constants.MAXLEN_MATERIAL_MARK_DATA)
    mark_type = models.IntegerField()
    permissions = models.IntegerField()


class Author(models.Model):
    name = models.ForeignKey(AuthorName, on_delete=models.SET_NULL, null=True)
