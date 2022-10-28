# -*- coding:utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url

import api

urlpatterns = [
    url(r'^v1/certificate/', api.get_uar_certificate_data, name='certificate_student_data'),
]
