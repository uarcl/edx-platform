# -*- coding:utf-8 -*-

from django.conf import settings
from django.urls import path, re_path
from . import api

urlpatterns = [
    re_path(
        r'^(?P<certificate_uuid>[0-9a-f]{32})$',
        api.get_uar_certificate_data,
        name='certificate_student_data'
    ),
]
