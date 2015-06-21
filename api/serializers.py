from models import Wuser,WuserPreference,WuserPhoto,WuserRelations,WuserProperties,Chats,WuserChats,Events,WuserEvents
from rest_framework import serializers


class WuserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wuser
        fields = ('id','email','password','name','display_name',
            'current_country','current_city','gender',
            'date_of_birth','college_country',
            'college_name','sign_up_type',
            'is_reported_abuse','last_login',
            'time_created')


class WuserPreferenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserPreference
        fields = ('id','wuser_id','pref_type','pref')

class WuserPropertiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserProperties
        fields = ('id','wuser_id','prop_type','prop_value')

class WuserPhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserPhoto
        fields = ('id','wuser_id','photo_type','photo','time_created','is_deleted','is_profile_photo','time_updated','is_enabled')

class WuserRelationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserRelations
        fields = ('id','wuser_id','counterparty','relation','is_active','time_created')

class ChatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chats
        fields = ('id','name','time_created')

class WuserChatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserChats
        fields = ('id','wuser_id','counterparty','chat_id','time_created','last_updated')

class EventsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Events
        fields = ('id','name','description','creator_id','venue','event_date','time_created')

class WuserEventsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserEvents
        fields = ('id','wuser_id','event_id','time_created')


