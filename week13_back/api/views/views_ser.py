import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Company
from api.serializers import CompanySerializerS

@csrf_exempt
def company_list_ser(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializerS(companies, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        request_body = json.loads(request.body)

        serializer = CompanySerializerS(data=request_body)
        if serializer.is_valid():  # Validate data from client
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.errors})


@csrf_exempt
def company_detail_ser(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = CompanySerializerS(company)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        request_body = json.loads(request.body)

        serializer = CompanySerializerS(instance=company, data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.errors})

    # Delete selected object
    elif request.method == 'DELETE':
        company.delete()

        return JsonResponse({'deleted': True})