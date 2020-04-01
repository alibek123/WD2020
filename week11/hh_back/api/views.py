import json

from django.core import serializers
from django.db.models import F

from django.http import JsonResponse, Http404
from api.models import Company, Vacancy


def companies_list(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)


def company_details(request, com_id):
    try:
        company = Company.objects.get(id=com_id)
    except Company.DoesNotExist:
        raise Http404

    return JsonResponse(company.to_json())


def company_vacancies(request, com_id):
    company = Company.objects.get(id=com_id)
    vacancies = company.vacancy_set.all().values()
    return JsonResponse({'Vacancies': list(vacancies)})


def vacancies_list(request):
    vacancies_json = list(Vacancy.objects.values())
    return JsonResponse(vacancies_json, safe=False)


def vacancy_details(request, vac_id):
    vacancy = Vacancy.objects.values()
    vacancy_det = vacancy.get(id=vac_id)
    return JsonResponse(vacancy_det, safe=False)


def vacancy_top_10(request):
    vacancy = list(Vacancy.objects.values().order_by(F('salary').desc())[:10])
    return JsonResponse(vacancy, safe=False)