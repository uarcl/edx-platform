# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from model_utils import Choices
from django.core.exceptions import ValidationError
from opaque_keys.edx.django.models import CourseKeyField
from django.utils.translation import ugettext_lazy as _

from opaque_keys import InvalidKeyError
from opaque_keys.edx.keys import CourseKey

class CertificateUar(models.Model):

    course_id = CourseKeyField(max_length=255, db_index=True, unique=True,verbose_name=_('course'))
    AdicText = models.CharField(verbose_name=u'Texto Adicional',max_length=100)
    Format =  models.CharField(verbose_name=u'Formato',max_length=30,default=u'uar')
    Chours = models.IntegerField(verbose_name=u'Horas Curso',default=0)

    class Meta(object):
        ordering = ('course_id',)
