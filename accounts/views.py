from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

User = get_user_model()


# ================ SIGNUP VIEW ==================== #

class SignupView(APIView):
    """
    Signup View to allow user registration.

    For more detail [see here][ref].

    [ref]: http://localhost:8000/api/accounts/signup

    With APIView, we have more controle on data structuring

    """
    permission_classes = (permissions.AllowAny,) # allow any access

    def post(self, request, format=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists. Please used another one!'})
            else:
                if len(password) < 6:
                    return Response({'error': 'Password must at least 6 characters'})
                else:
                    user = User.objects.create_user(email=email, name=name, password=password)
                    user.save()
                    return Response({'success': 'User created Successfully!'})
        else:
            return Response({'error': 'Password do not match'})

