from models import Wuser,WuserPreference,WuserPhoto,WuserRelations,WuserProperties,Chats,WuserChats,Events,WuserEvents
from rest_framework import serializers

def update_id(func):
    '''A decorator for pulling a data object's ID value out of a
       user-defined sequence.  This gets around a limitation in 
       django whereby we cannot supply our own sequence names.'''
    
    def decorated_function(*args):
        # Grab a reference to the data object we want to update.
        for name, value in args.items():
            print '{key} = {value}'.format(name, value)

        data_object = args[0]
        
        # Only update the ID if there isn't one yet.
        if data_object.id is None:
            # Construct the new sequence name based on the table's meta data.
            sequence_name = '%s_seq' % data_object._meta.db_table
        
            # Query the database for the next sequence value.
            from django.db import connection
            cursor = connection.cursor()
            cursor.execute("SELECT nextval(%s)", [sequence_name])
            row = cursor.fetchone()
        
            # Update the data object's ID with the returned sequence value.
            data_object.id = row[0]
        
        # Execute the function we're decorating.
        return func(*args)
    
    return decorated_function

class WuserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wuser
        fields = ('id','email','password','name','display_name',
            'current_country','current_city','gender',
            'date_of_birth','college_country',
            'college_name','sign_up_type',
            'is_reported_abuse','last_login',
            'time_created')
        
    def create(self, validated_data):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT nextval('wuser_id_seq')")
        row = cursor.fetchone()
        user = Wuser(
            id=row[0],
            email=validated_data['email'],
            name=validated_data['name'],
            current_city=validated_data['current_city']
            
        )
        user.save()
        return user


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
        fields = ('id','wuser_id','photo_name','time_created','is_deleted','is_profile_photo',
            'time_updated','is_enabled','mask_id')

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


