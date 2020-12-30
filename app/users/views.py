from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status, viewsets, permissions, generics

from users.models import User, Profile
from users.serializers import UserNestedSerializers, ProfileSerializers, UserSerializers
from rest_framework.decorators import api_view, action, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated


class UsersNestedViewSet(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserNestedSerializers


class ProfileListView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers


class ProfileViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializers
    queryset = Profile.objects.all()


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UsersViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()


# class UsersViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers
#     lookup_field = 'id'

    # @action(detail=True, methods=['put'])
    # @parser_classes(parser_classes=JSONParser)
    # users_data = JSONParser().parse(request, pk)
    # users_serializer = UserSerializers(users, data=users_data)
    # if users_serializer.is_valid():
    #     users_serializer.save()
    #     return JsonResponse(users_serializer.data)
    # return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# TODO: search reference to post and request image
    # @api_view(['GET', 'POST'])
    # def users_list(request):
    #     if request.method == 'GET':
    #         user = User.objects.all()

    #         username = request.GET.get('username', None)
    #         if username is not None:
    #             user = user.filter(username__icontains=username)

    #         users_serializer = UserSerializers(user, many=True)
    #         return JsonResponse(users_serializer.data, safe=False)
    #         # 'safe=False' for objects serialization

    #     elif request.method == 'POST':
    #         users_data = JSONParser().parse(request)
    #         users_serializer = UserSerializers(data=users_data)
    #         if users_serializer.is_valid():
    #             users_serializer.save()
    #             return JsonResponse(users_serializer.data, status=status.HTTP_201_CREATED)
    #         return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @api_view(['DELETE'])
    # @permission_classes([IsAuthenticated])
    # def user_delete(request, format=None):
    #     count = User.objects.all().delete()
    #     return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

    # @api_view(['GET', 'POST'])
    # def profile_list(request):
    #     if request.method == 'GET':
    #         profile = Profile.objects.all()

    #         nama = request.GET.get('nama', None)
    #         if nama is not None:
    #             profile = profile.filter(nama__icontains=nama)

    #         profile_serializer = ProfileSerializers(profile, many=True)
    #         return JsonResponse(profile_serializer.data, safe=False)
    #         # 'safe=False' for objects serialization

    #     elif request.method == 'POST':
    #         profile_data = JSONParser().parse(request)
    #         profile_serializer = ProfileSerializers(data=profile_data)
    #         if profile_serializer.is_valid():
    #             profile_serializer.save()
    #             return JsonResponse(profile_serializer.data, status=status.HTTP_201_CREATED)
    #         return JsonResponse(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @api_view(['GET', 'PUT'])
    # def user_detail(request, pk):
    #     try:
    #         users = User.objects.get(pk=pk)
    #     except User.DoesNotExist:
    #         return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    #     if request.method == 'GET':
    #         users_serializer = UserSerializers(users)
    #         return JsonResponse(users_serializer.data)

    #     elif request.method == 'PUT':
    #         users_data = JSONParser().parse(request)
    #         users_serializer = UserSerializers(users, data=users_data)
    #         if users_serializer.is_valid():
    #             users_serializer.save()
    #             return JsonResponse(users_serializer.data)
    #         return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #     elif request.method == 'DELETE':
    #         users.delete()
    #         return JsonResponse({'message': 'Users was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    # @api_view(['GET', 'PUT'])
    # def profile_detail(request, pk):
    #     try:
    #         profile = Profile.objects.get(pk=pk)
    #     except Profile.DoesNotExist:
    #         return JsonResponse({'message': 'The profile does not exist'}, status=status.HTTP_404_NOT_FOUND)

    #     if request.method == 'GET':
    #         profile_serializer = ProfileSerializers(profile)
    #         return JsonResponse(profile_serializer.data)

    #     elif request.method == 'PUT':
    #         profile_data = JSONParser().parse(request)
    #         profile_serializer = ProfileSerializers(profile, data=profile_data)
    #         if profile_serializer.is_valid():
    #             profile_serializer.save()
    #             return JsonResponse(profile_serializer.data)
    #         return JsonResponse(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     profile.delete()
    #     return JsonResponse({'message': 'profile was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# class UsersViewSet(viewsets.ModelViewSet):
#     queryset = Users.objects.all()
#     serializer_class = UsersSerializers
#     permission_classes = [permissions.IsAuthenticated]

#     @action(detail=True)
#     def

# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializers
#     permission_classes = [permissions.IsAuthenticated]

# @api_view(['GET'])
# def users_list_published(request):
#     return JsonResponse(usersViewSet.serializer_class.data, safe=False,)
