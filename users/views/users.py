#Django REST framework
from users import serializers
from rest_framework import status
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from users.permissions import IsOwnProfile
from django.http import HttpResponseRedirect

#models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from users.models import Profile

#Serializer
from users.serializers.users import UserSerializer
from users.serializers.signup import UserSignupSerializer
from users.serializers.verify import AccountVerificationSerializer
from users.serializers.users import NewUserSerializer, UserSerializer

class UserListView (ListAPIView):
    """ List of all the users with pagination """
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    
    
class ProfileCompletionViewSet(mixins.UpdateModelMixin,
                               mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    ''' Complete a user information data'''

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[IsAuthenticated, IsOwnProfile]


@api_view(['POST'])
def signup(request):

    if request.method == 'POST':
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = NewUserSerializer(user).data
        return Response(data)

@api_view(['GET'])
def account_verification(request, token):
    """Account verification API View"""
    if request.method == 'GET':
        token = request.path.split('/')
        token = token[3]
        data = {'token':f'{token}'}
        serializer = AccountVerificationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message':'account verified successfully'}
        return HttpResponseRedirect("https://sleepy-heisenberg-78d033.netlify.app/verification/%22)
