from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from coffee_types.models import Coffee
from coffee_types.serializers import CoffeeSerializer


class ManageListingView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user

            if not user.is_manager and not user.is_baristas and not user.is_superuser:
                return Response(
                    {'error': 'You do not have necessary permissions for getting this list data'},
                    status=status.HTTP_403_FORBIDDEN
                )
            
            # retrieve the slug
            slug = request.query_params.get('slug')
            
            # if slug was not passed in query-params then
            # retrieve the coffees related to that store_manager
            if not slug:
                coffee = Coffee.objects.order_by('-date_created').filter(
                    store_manager_email=user.email
                )
                # serialize the data and sent it back
                coffee = CoffeeSerializer(coffee, many=True)
                
                return Response(
                    {'coffees_list': coffee.data},
                    status=status.HTTP_200_OK
                )
            # if slug was passed, retrieve that particular coffee with that slug
            # sent it back in Response
            if not Coffee.objects.filter(
                store_manager_email=user.email,
                slug=slug
            ).exists():
                return Response(
                    {'error': 'Coffee not found'},
                    status=status.HTTP_404_NOT_FOUND
                )

            coffee = Coffee.objects.get(store_manager_email=user.email, slug=slug)
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
            

    def post(self, request):
        try:
            user = request.user

            if not user.is_manager and not user.is_superuser:
                return Response(
                    {'error': 'User does not have necessary permissions'},
                    status=status.HTTP_403_FORBIDDEN
                )

            data = request.data

            title = data['title']
            slug = data['slug']
            description = data['description']
            price = data['price']
            coffee_type = data['coffee_type']
            
            if coffee_type == 'FOR_PREMIUM_USERS':
                coffee_type = 'For Premium'
            else:
                coffee_type = 'For regular'
            
            main_photo = data['main_photo']
            photo_1 = data['photo_1']
            photo_2 = data['photo_2']
            is_published = data['is_published']

            if is_published == 'True':
                is_published = True
            else:
                is_published = False

            if Coffee.objects.filter(slug=slug).exists():
                return Response(
                    {'error': 'Listing with this slug already exists'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            Coffee.objects.create(
                store_manager_email=user.email,
                title=title,
                slug=slug,
                description=description,
                price=price,
                coffee_type=coffee_type,
                main_photo=main_photo,
                photo_1=photo_1,
                photo_2=photo_2,
                is_published=is_published
            )

            return Response(
                {'success': 'A new Coffee created successfully'},
                status=status.HTTP_201_CREATED
            )
        except:
            return Response(
                {'error': 'Something went wrong when creating new coffee'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
    def put(self, request):
        try:
            user = request.user
            if not user.is_manager:
                return Response(
                    {'error': 'You dont have permission'},
                    status=status.HTTP_403_FORBIDDEN
                )
            data = request.data
            title = data['title']
            slug = data['slug']
            description = data['description']
            price = data['price']
            coffee_type = data['coffee_type']
            
            if coffee_type == 'FOR_PREMIUM_USERS':
                coffee_type = 'For Premium'
            else:
                coffee_type = 'For regular'
            
            main_photo = data['main_photo']
            photo_1 = data['photo_1']
            photo_2 = data['photo_2']
            is_published = data['is_published']

            if is_published == 'True':
                is_published = True
            else:
                is_published = False

            Coffee.objects.update(
                title=title,
                slug=slug,
                description=description,
                price=price,
                coffee_type=coffee_type,
                main_photo=main_photo,
                photo_1=photo_1,
                photo_2=photo_2,
                is_published=is_published
            )

            return Response(
                {'success': 'Coffee details updated successfully'},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'You dont have permission'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    def patch(self, request):
        try:
            user = request.user

            if not user.is_manager and not user.is_superuser:
                return Response(
                    {'error': 'User does not have necessary permissions'},
                    status=status.HTTP_403_FORBIDDEN
                )

            data = request.data

            slug = data['slug']

            is_published = data['is_published']
            if is_published == 'True':
                is_published = True
            else:
                is_published = False

            if not Coffee.objects.filter(
                store_manager_email=user.email,
                slug=slug
            ).exists():
                return Response(
                    {'error': 'Coffee does not exist'},
                    status=status.HTTP_404_NOT_FOUND
                )

            Coffee.objects.filter(
                store_manager_email=user.email,
                slug=slug
            ).update(
                is_published=is_published
            )

            return Response(
                {'success': 'Coffee publish status updated successfully'},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when updating listing'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
