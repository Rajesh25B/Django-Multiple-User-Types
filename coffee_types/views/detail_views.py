from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from coffee_types.models import Coffee
from coffee_types.serializers import CoffeeSerializer


class CoffeeDetailView(APIView):
    '''
    Restricted View
    Returns a particular coffee based on slug
    '''
    def get(self, request, format=None):
        try:
            slug = request.query_params.get('slug')

            if not slug:
                return Response(
                    {'error': 'Must provide slug'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if not Coffee.objects.filter(slug=slug, is_published=True).exists():
                return Response(
                    {'error': 'Coffee does not exist'},
                    status=status.HTTP_404_NOT_FOUND
                )

            coffee = Coffee.objects.get(slug=slug, is_published=True)
            coffee = CoffeeSerializer(coffee)

            return Response(
                {'coffee': coffee.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when retrieving coffee detail'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            

class CoffeeListView(APIView):
    '''Returns all types of coffee for unrestricted access '''
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        try:
            if not Coffee.objects.filter(is_published=True).exists():
                return Response(
                    {'error': 'Not available'},
                    status=status.HTTP_404_NOT_FOUND
                )

            coffee = Coffee.objects.filter(is_published=True)
            coffee = CoffeeSerializer(coffee, many=True)

            return Response(
                {'available_coffee': coffee.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when retrieving coffee'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
