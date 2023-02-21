# -*- coding:utf-8 -*-
from django.contrib import admin
from django import forms
from xmodule.modulestore.django import modulestore
from opaque_keys import InvalidKeyError
from opaque_keys.edx.keys import CourseKey
from django.core.exceptions import ValidationError
from opaque_keys.edx.locations import SlashSeparatedCourseKey

from .models import CertificateUar

class CertificateUarAdminForm(forms.ModelForm):
    class Meta(object):
        model = CertificateUar
        fields = '__all__'

    def clean_course_id(self):
        course_id = self.cleaned_data['course_id']
        try:
            course_key = CourseKey.from_string(course_id)
        except InvalidKeyError:
            try:
                course_key = SlashSeparatedCourseKey.from_deprecated_string(course_id)
            except InvalidKeyError:
                raise forms.ValidationError("Cannot make a valid CourseKey from id {}!".format(course_id))

        if not modulestore().has_course(course_key):
            raise forms.ValidationError("Cannot find course with id {} in the modulestore".format(course_id))

        return course_key

    def save(self,commit=True):
        return super(CertificateUarAdminForm,self).save(commit=commit)

class CertificateUarAdmin(admin.ModelAdmin):
    form = CertificateUarAdminForm
    fields = ('course_id','AdicText','Format','Chours')
    search_fields = ('course_id',)
    list_display =  ('course_id','AdicText','Format','Chours')

admin.site.register(CertificateUar,CertificateUarAdmin)

