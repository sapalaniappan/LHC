from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.db.models import Q
from api.models import Wuser,WuserPreference,WuserPhoto,WuserRelations,WuserProperties,WuserChats,WuserEvents,Events
from api.serializers import WuserSerializer,WuserPreferenceSerializer,WuserPhotoSerializer,WuserRelationsSerializer,WuserPropertiesSerializer,WuserChatsSerializer,WuserEventsSerializer,EventsSerializer,WuserDetailSerializer

from rest_framework.generics import ListAPIView
from itertools import chain

#class ResultsList(ListAPIView):
#    def list(self, request, *args, **kwargs):
#        #user = Wuser.objects.all()
#        user = Wuser.objects.get(pk=162)
#        photos = WuserPhotos.objects.filter(wuser_id=162)
#
#        results = list()
#        entries = list(chain(photos)) # combine the two querysets
#        results.append(user)
#        results.append(photos)   
#        return Response(results)

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
        data=request.DATA
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT nextval('wuser_id_seq')")
        row = cursor.fetchone()
        data['id']=row[0]
        serializer = WuserSerializer(data=data)
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

@api_view(['GET'])
def user_detail_by_email(request, email):
    """
    Get, udpate, or delete a specific user
    """
    try:
        user = Wuser.objects.get(email=email)
    except Wuser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WuserSerializer(user)
        return Response(serializer.data)


@api_view(['GET'])
def user_full_detail_by_email(request, email):
    """
    Get, udpate, or delete a specific user
    """
    try:
        user = Wuser.objects.get(email=email)
        user_photos = list(WuserPhoto.objects.filter(wuser_id=user.id))
        #combined=(user,user_photos)
    except Wuser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WuserDetailSerializer(user)
        #data= serializers.serialize('json',combined)
        return Response(serializer.data)

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

    elif request.method == 'POST':
        data=request.DATA
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT nextval('wuser_preference_id_seq')")
        row = cursor.fetchone()
        data['id']=row[0]
        serializer = WuserPreferenceSerializer(data=data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
def user_photos(request, id):
    """
    Get, udpate, or delete a specific user's Photos
    """
    if request.method == 'POST':
        data=request.DATA
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT nextval('wuser_photo_id_seq')")
        row = cursor.fetchone()
        data['id']=row[0]
        serializer = WuserPhotoSerializer(data=data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    try:
        user_photos = WuserPhoto.objects.filter(wuser_id=id)
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

@api_view(['GET', 'PUT','POST', 'DELETE'])
def user_properties(request, userid):
    """
    Get, udpate, or delete a specific user's Properties
    """
    if request.method == 'POST':
        data=request.DATA
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT nextval('wuser_properties_id_seq')")
        row = cursor.fetchone()
        data['id']=row[0]
        serializer = WuserPropertiesSerializer(data=data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    try:
        user_properties = WuserProperties.objects.filter(wuser_id=userid)
    except WuserProperties.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WuserPropertiesSerializer(user_properties,many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WuserPropertiesSerializer(user_properties, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

#user Chats
@api_view(['GET', 'PUT','POST', 'DELETE'])
def user_chats(request, id):
    """
    Get, udpate, or delete a specific user's Chat Info
    """
    if request.method == 'POST':
        data=request.DATA
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT nextval('wuser_chats_id_seq')")
        row = cursor.fetchone()
        data['id']=row[0]
        serializer = WuserChatsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    try:
        user_chats = WuserChats.objects.filter( Q(wuser_id=id) | Q(counterparty=id))
    except WuserChats.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WuserChatsSerializer(user_chats,many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WuserChatsSerializer(user_chats, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

#WuserRelations
@api_view(['GET', 'PUT', 'POST' , 'DELETE'])
def user_relations(request, id):
    """
    Get, udpate, or delete a specific  user_relations
    """
    if request.method == 'POST':
        data=request.DATA
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT nextval('wuser_relations_id_seq')")
        row = cursor.fetchone()
        data['id']=row[0]
        serializer = WuserRelationsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    try:
        user_relations = WuserRelations.objects.get( Q(wuser_id=id) | Q(counterparty=id))
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


@api_view(['GET', 'PUT', 'POST' , 'DELETE'])
def user_events(request, id):
    """
    Get, udpate, or delete a specific  user_event
    """
    if request.method == 'POST':
        data=request.DATA
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT nextval('wuser_events_id_seq')")
        row = cursor.fetchone()
        data['id']=row[0]
        serializer = WuserEventsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    try:
        user_events = WuserEvents.objects.get(wuser_id=id)
    except WuserEvents.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WuserEventsSerializer(user_events)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WuserEventsSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'POST' , 'DELETE'])
def events(request, id):
    """
    Get, udpate, or delete a specific  user_event
    """
    if request.method == 'POST':
        data=request.DATA
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT nextval('events_id_seq')")
        row = cursor.fetchone()
        data['id']=row[0]
        serializer = EventsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    try:
        events = Events.objects.get(pk=id)
    except Events.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventsSerializer(events)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EventsSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserView(ListAPIView):
    """
    Returns a list of all authors.
    """
    model = Wuser
    serializer_class = WuserDetailSerializer
    #queryset = Wuser.objects.get(pk=id)

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        #queryset = super(UserView, self).get_queryset()
        #serializer = WuserDetailSerializer(queryset, many=False)
        #id = self.kwargs['id']
        return Wuser.objects.get(pk=self.kwargs.get('id')) 

    def list(self, request, id):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = WuserDetailSerializer(queryset, many=False)
        return Response(serializer.data)

class UserEmail(ListAPIView):
    """
    Returns a list of all authors.
    """
    model = Wuser
    serializer_class = WuserDetailSerializer
    #queryset = Wuser.objects.get(pk=id)

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        #queryset = super(UserView, self).get_queryset()
        #serializer = WuserDetailSerializer(queryset, many=False)
        #id = self.kwargs['email']
        return Wuser.objects.get(email=self.kwargs.get('email'))

    def list(self, request, email):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = WuserDetailSerializer(queryset, many=False)
        return Response(serializer.data)
