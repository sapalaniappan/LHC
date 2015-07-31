from django.db import models


# Create your models here.

class Wuser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    email = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    age = models.DecimalField(max_digits=65535, decimal_places=0, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    display_name = models.TextField(blank=True, null=True)
    current_country = models.TextField(blank=True, null=True)
    current_city = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    date_of_birth = models.CharField(max_length=20, blank=True, null=True)
    college_country = models.TextField(blank=True, null=True)
    college_name = models.TextField(blank=True, null=True)
    sign_up_type = models.CharField(max_length=1, blank=True, null=True)
    is_reported_abuse = models.NullBooleanField()
    last_login = models.DateTimeField(blank=True, null=True)
    time_created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wuser'


class WuserPhoto(models.Model):
    id = models.BigIntegerField(primary_key=True)
    wuser_id = models.BigIntegerField()
    photo_name = models.CharField(max_length=10, blank=True, null=True)
    time_created = models.DateTimeField(blank=True, null=True)
    is_deleted = models.NullBooleanField()
    is_profile_photo = models.NullBooleanField()
    time_updated = models.DateTimeField(blank=True, null=True)
    is_enabled = models.NullBooleanField()
    mask_id = models.DecimalField(max_digits=65535, decimal_places=0, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'wuser_photo'
    
    
class WuserPreference(models.Model):
    id = models.BigIntegerField(primary_key=True)
    wuser_id = models.DecimalField(max_digits=65535, decimal_places=0, blank=True, null=True)
    pref_type = models.CharField(max_length=10, blank=True, null=True)
    pref = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wuser_preference'


class WuserProperties(models.Model):
    id = models.BigIntegerField(primary_key=True)
    wuser_id = models.DecimalField(max_digits=65535, decimal_places=0, blank=True, null=True)
    prop_type = models.CharField(max_length=10, blank=True, null=True)
    prop_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wuser_properties'

class WuserRelations(models.Model):
    id = models.BigIntegerField(primary_key=True)
    wuser_id = models.DecimalField(max_digits=65535, decimal_places=0, blank=True, null=True)
    counterparty = models.DecimalField(max_digits=65535, decimal_places=0, blank=True, null=True)
    relation = models.DecimalField(max_digits=65535, decimal_places=0, blank=True, null=True)
    is_active = models.NullBooleanField()
    time_created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wuser_relations'

class Chats(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    time_created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chats'


class WuserChats(models.Model):
    id = models.BigIntegerField(primary_key=True)
    wuser_id = models.DecimalField(max_digits=65535, decimal_places=0, blank=True, null=True)
    counterparty = models.DecimalField(max_digits=65535, decimal_places=0, blank=True, null=True)
    chat_id = models.DecimalField(max_digits=65535, decimal_places=0, blank=True, null=True)
    time_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wuser_chats'

class Events(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.DecimalField(max_digits=65535, decimal_places=0, blank=True, null=True)
    venue = models.CharField(max_length=60, blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    time_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    access_code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


class WuserEvents(models.Model):
    id = models.BigIntegerField(primary_key=True)
    wuser_id = models.DecimalField(max_digits=65535, decimal_places=0, blank=True, null=True)
    event_id = models.DecimalField(max_digits=65535, decimal_places=0, blank=True, null=True)
    time_created = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'wuser_events'

