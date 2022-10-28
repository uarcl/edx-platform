# -*- coding:utf-8 -*-
import logging
from django.db import models
from .models import CertificateUar
from lms.djangoapps.certificates.models import (
    GeneratedCertificate,
    CertificateStatuses
)
from openedx.core.djangoapps.content.course_overviews.api import get_course_overview_or_none
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from util.json_request import JsonResponse
from django.http.response import HttpResponseBadRequest

log = logging.getLogger(__name__)

@csrf_exempt
def get_uar_certificate_data(request):
    if request.method == 'GET':
        try:
            certificate = GeneratedCertificate.eligible_certificates.get(
                verify_uuid=request.uuid,
                status=CertificateStatuses.downloadable
            )
            try:
                course_overview = get_course_overview_or_none(certificate.course)
                if not course_overview:
                    return JsonResponse(status=404)
                certificate_format = CertificateUar.get(course=certificate.course)
                return JsonResponse({'cert_uid':certificate.verify_uuid,
                                     'cert_status':certificate.status,
                                     'cert_mode':certificate.mode,
                                     'cert_created_date':certificate.created_date,
                                     'cert_text_adic':certificate_format.AdicText,
                                     'cert_course_hours':certificate_format.Chours,
                                     'cert_format':certificate_format.Format,
                                     'student_name':certificate.name,
                                     'cert_student_doc_number':certificate.document_number,
                                     'course_name':course_overview.display_name,
                                     'course_cert_name':course_overview.cert_name_short,
                                     })
            except CertificateUar.DoesNotExist:
                return JsonResponse(status=404)
        except GeneratedCertificate.DoesNotExist:
            return JsonResponse(status=404)
    return HttpResponseBadRequest(u'Ha ocurrido un error')
