# -*- coding:utf-8 -*-
from .models import CertificateUar
from opaque_keys.edx import locator

def get_cert_adic_text(course_id):
    try:
        course = locator.CourseLocator.from_string(course_id)
        custom_cert =  CertificateUar.objects.get(course_id=course)
        return custom_cert.AdicText
    except CertificateUar.DoesNotExist:
        return ''

