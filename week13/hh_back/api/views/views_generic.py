from rest_framework import generics

from api.models import Vacancy
from api.serializers import VacancySerializer


class VacancyListAPIView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
