from django.urls import path

from api.views import companies_list, company_details, company_vacancies, vacancies_list, vacancy_details, \
    vacancy_top_10

urlpatterns = [
    path('companies/', companies_list),
    path('companies/<int:com_id>/', company_details),
    path('companies/<int:com_id>/vacancies/', company_vacancies),
    path('vacancies/', vacancies_list),
    path('vacancies/<int:vac_id>/', vacancy_details),
    path('vacancies/top_ten/', vacancy_top_10),
]
