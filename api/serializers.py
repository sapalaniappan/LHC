from models import Wuser,WuserPreference,WuserPhoto,WuserRelations
from rest_framework import serializers


class WuserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wuser
        fields = ('id','email','name','display_name','current_country','current_city','gender','date_of_birth','college_country','college_name','sign_up_type','is_reported_abuse','last_login','time_created')


class WuserPreferenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserPreference
        fields = ('id','wuser_id','pref_type','pref')

class WuserPhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserPhoto
        fields = ('id','wuser_id','photo_type','photo','time_created','is_deleted','is_profile_photo','time_updated','is_enabled')

class WuserRelationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WuserRelations
        fields = ('id','wuser_id','like_from_id','like_to_id','passed_id','time_created')
