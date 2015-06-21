from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Wuser,WuserPreference,WuserPhoto,WuserRelations
from api.serializers import WuserSerializer,WuserPreferenceSerializer,WuserPhotoSerializer,WuserRelationsSerializer


@api_view(['GET', 'POST'])
def user_list(request):
    """
    List all users, or create a new user.
    """
    if request.method == 'GET':
        users = Wuser.objects.all()
        serializer = WuserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WuserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """
    Get, udpate, or delete a specific user
    """
    try:
        user = Wuser.objects.get(pk=pk)
    except Wuser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WuserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WuserSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Wuser Preference
@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def user_preferences(request, id):
    """
    Get, udpate, or delete a specific user's Preference
    """
    try:
        user_pref = WuserPreference.objects.get(wuser_id=id)
    except WuserPreference.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WuserPreferenceSerializer(user_pref)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WuserPreferenceSerializer(user_pref, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user_pref.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# #WuserPhoto
# @api_view(['GET', 'PUT','POST', 'DELETE'])
# def user_photos_by_id(request, pk):
#     """
#     Get, udpate, or delete a specific user's Photos
#     """
#     try:
#         user_photo = WuserPhoto.objects.get(pk=pk)
#     except WuserPhoto.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = WuserPhotoSerializer(user_photo)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = WuserPhotoSerializer(user_photo, data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(
#                 serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         user_photo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#WuserPhotos
@api_view(['GET', 'PUT','POST', 'DELETE'])
def user_photos_by_user(request, id):
    """
    Get, udpate, or delete a specific user's Photos
    """
    try:
        user_photos = WuserPhoto.objects.get(wuser_id=id)
    except WuserPhoto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WuserPhotoSerializer(user_photos,many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WuserPhotoSerializer(user_photos, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     user_photos.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

#WuserRelations
@api_view(['GET', 'PUT', 'DELETE'])
def user_relations(request, id):
    """
    Get, udpate, or delete a specific  user_relations
    """
    try:
        user_relations = WuserRelations.objects.get(wuser_id=id)
    except WuserRelations.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WuserRelationsSerializer(user_relations)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WuserRelationsSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



