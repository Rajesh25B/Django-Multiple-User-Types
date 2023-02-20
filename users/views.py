from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import UserSerializer

User = get_user_model()


class RegisterView(APIView):
    '''
    Registering user accounts
    '''
    permission_classes = [permissions.AllowAny, ]
    
    def post(self, request):
        try:
            data = request.data

            email = data['email']
            email = email.lower()
            name = data['name']

            password = data['password']
            re_password = data['re_password']

            is_baristas = data['is_baristas']
            is_manager = data['is_manager']
            is_accountant = data['is_accountant']
            
            is_baristas = True if is_baristas == 'True' else False
            is_manager = True if is_manager == 'True' else False
            is_accountant = True if is_accountant == 'True' else False
            
            if password == re_password:
                if len(password) >= 8:
                    if not User.objects.filter(email=email).exists():
                        if not is_manager and not is_accountant and not is_baristas:
                            User.objects.create_user(
                                email=email,
                                name=name,
                                password=password
                            )
                            return Response(
                                {'success': 'User created successfully'},
                                status=status.HTTP_201_CREATED
                            )
                        elif not is_accountant and not is_baristas:
                            User.objects.create_manager(
                                email=email,
                                name=name,
                                password=password
                            )
                            return Response(
                                {'success': 'Manager created successfully'},
                                status=status.HTTP_201_CREATED
                            )
                        elif not is_manager and not is_baristas:
                            User.objects.create_accountant(
                                email=email,
                                name=name,
                                password=password
                            )
                            return Response(
                                {'success': 'Accountant created successfully'},
                                status=status.HTTP_201_CREATED
                            )
                        elif not is_accountant and not is_manager:
                            User.objects.create_baristas(
                                email=email,
                                name=name,
                                password=password
                            )
                            return Response(
                                {'success': 'Barista created successfully'},
                                status=status.HTTP_201_CREATED
                            )

                    else:
                        return Response(
                            {'error': 'User with this e-mail already exists'},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                
                else:
                    return Response(
                    {'error': 'passwords must be 8 characters'},
                    status=status.HTTP_400_BAD_REQUEST
                )
                    
            
            else:
                return Response(
                    {'error': 'passwords do not match'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except:
            return Response(
                {'error': 'Something went wrong'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
                        


class RetrieveUserView(APIView):
    '''
    Retrieving the user data
    '''
    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)

            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when retrieving user details'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )