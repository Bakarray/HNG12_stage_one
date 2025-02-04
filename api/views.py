from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import is_prime, is_perfect, get_properties, get_digit_sum, get_fun_fact

# Create your views here.
class NumberClassificationView(APIView):
    def get(self, request, format=None):
        number_param = request.query_params.get('number')

        if not number_param or not number_param.isdigit():
            return Response({
            "number": number,
            "error": 'true'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        number = int(number_param)

        response_data = {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": get_properties(number),
            "digit_sum": get_digit_sum(number),
            "fun_fact": get_fun_fact(number),
        }
        
        return Response(response_data, status=status.HTTP_200_OK)