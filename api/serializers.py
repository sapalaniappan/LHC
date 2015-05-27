from models import Wuser, WuserPhoto, WuserPreference, WuserRelations,
from rest_framework import serializers


class WuserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wuser
        fields = ('id','email','name','display_name','current_country','current_city','gender','date_of_birth','college_country','college_name','sign_up_type','is_reported_abuse','last_login','time_created')
