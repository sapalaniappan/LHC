from models import WuserNotificationsUpdate,WuserNotifications,WuserDevicesUpdate,WuserDevices,WuserPhotoUpdate,Wuser,WuserPreference,WuserPhoto,WuserRelations,WuserProperties,Chats,WuserChats,Events,WuserEvents,WuserPreferenceUpdate,WuserRelationsUpdate,WuserPropertiesUpdate,WuserChatsUpdate,WuserEventsUpdate
from rest_framework import serializers


class WuserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wuser
        fields = ('id','email','password','name','display_name',
            'current_country','current_city','gender',
            'date_of_birth','college_country',
            'college_name','sign_up_type',
            'is_reported_abuse','last_login',
            'time_created','age')
        
    # def create(self, validated_data):
    #     from django.db import connection
    #     cursor = connection.cursor()
    #     cursor.execute("SELECT nextval('wuser_id_seq')")
    #     row = cursor.fetchone()
    #     user = Wuser(
    #         id=row[0],
    #         email=validated_data['email'],
    #         name=validated_data['name'],
    #         current_city=validated_data['current_city']
            
    #     )
    #     user.save()
    #     return user


class WuserPreferenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserPreference
        fields = ('id','pref_type','pref')

class WuserPreferenceUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserPreferenceUpdate
        fields = ('id','wuser_id','pref_type','pref')

class WuserPropertiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserProperties
        fields = ('id','prop_type','prop_value')

class WuserPropertiesUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserPropertiesUpdate
        fields = ('id','wuser_id','prop_type','prop_value')

class WuserPhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserPhoto
        fields = ('id','photo_name','time_created','is_deleted','is_profile_photo',
            'time_updated','is_enabled','mask_id')

class WuserPhotoUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserPhotoUpdate
        fields = ('id','wuser_id','photo_name','time_created','is_deleted','is_profile_photo',
            'time_updated','is_enabled','mask_id')

class WuserRelationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserRelations
        fields = ('id','counterparty','relation','is_active','time_created')

class WuserRelationsUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserRelationsUpdate
        fields = ('id','wuser_id','counterparty','relation','is_active','time_created')

class ChatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chats
        fields = ('id','name','time_created')

class WuserChatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserChats
        fields = ('id','counterparty','chat_id','time_created','last_updated')

class WuserChatsUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserChatsUpdate
        fields = ('id','wuser_id','counterparty','chat_id','time_created','last_updated')

class EventsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Events
        fields = ('id','name','description','creator_id','venue','event_date','time_created','city','country','access_code')

class WuserEventsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserEvents
        fields = ('id','event_id','time_created')

class WuserEventsUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserEventsUpdate
        fields = ('id','wuser_id','event_id','time_created')

class WuserNotificationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserNotifications
        fields = ('id','notify_type','notification','is_active','time_created')

class WuserNotificationsUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserNotificationsUpdate
        fields = ('id','wuser_id','notify_type','notification','is_active','time_created')

class WuserDevicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserDevices
        fields = ('id','device_token','is_active','is_registered','time_created')

class WuserDevicesUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserDevicesUpdate
        fields = ('id','wuser_id','device_token','is_active','is_registered','time_created')


class WuserDetailSerializer(serializers.ModelSerializer):
    photos = WuserPhotoSerializer(many=True)
    events = WuserEventsSerializer(many=True)
    properties = WuserPropertiesSerializer(many=True) 
    chats = WuserChatsSerializer(many=True)
    relations = WuserRelationsSerializer(many=True)
    preferences = WuserPreferenceSerializer(many=True)
    notifs= WuserNotificationsSerializer(many=True)
    devices=WuserDevicesSerializer(many=True) 
    class Meta:
        model = Wuser
        serializer_class = WuserSerializer
        fields = ('id','email','password','name','display_name',
            'current_country','current_city','gender',
            'date_of_birth','college_country',
            'college_name','sign_up_type',
            'is_reported_abuse','last_login',
            'time_created','age','photos','events','properties','chats','relations','preferences','notifs','devices')


