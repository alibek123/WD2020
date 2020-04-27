from django.urls import path

from api.views import company_list, company_details, vacancy_list, \
    vacancy_details  # Function-based

from api.views.views_cb import CompanyListAPIView, CompanyDetailsAPIView, VacancyDetailsAPIView, \
    VacancyListAPIView, CompanyListWvacAPIView  # Class based

# from api.views.views_generic import VacancyListAPIView

from api.views.views_ser import company_list_ser, company_detail_ser  # serializer.Serializer

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),

    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:company_id>/', CompanyDetailsAPIView.as_view()),  # class-based
    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:vacancy_id>', VacancyDetailsAPIView.as_view()),
    path('companiesWv/', CompanyListWvacAPIView)

    # path('companies/', company_list),
    # path('companies/<int:company_id>/', company_details),     # function based
    # path('vacancies/', vacancy_list),
    # path('vacancies/<int:vacancy_id>/', vacancy_details),

    # path('companies/', company_list_ser),
    # path('companies/<int:company_id>/', company_detail_ser),  # serializer.Serializer

    # path('companies/<int:com_id>/vacancies/', company_vacancies),
    # path('vacancies/', vacancies_list),
    # path('vacancies/<int:vac_id>/', vacancy_details),
    # path('vacancies/top_ten/', vacancy_top_10),
]
