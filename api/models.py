from django.db import models

# Create your models here.

class Wuser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    email = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    display_name = models.TextField(blank=True, null=True)
    current_country = models.TextField(blank=True, null=True)
    current_city = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    date_of_birth = models.CharField(max_length=10, blank=True, null=True)
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
    wuser_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    photo_type = models.CharField(max_length=10, blank=True, null=True)
    photo = models.BinaryField(blank=True, null=True)
    time_created = models.DateTimeField(blank=True, null=True)
    is_deleted = models.NullBooleanField()
    is_profile_photo = models.NullBooleanField()
    time_updated = models.DateTimeField(blank=True, null=True)
    is_enabled = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'wuser_photo'
    
    
class WuserPreference(models.Model):
    id = models.BigIntegerField(primary_key=True)
    wuser_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pref_type = models.CharField(max_length=10, blank=True, null=True)
    pref = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wuser_preference'


class WuserRelations(models.Model):
    id = models.BigIntegerField(primary_key=True)
    wuser_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    like_from_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    like_to_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    passed_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    time_created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wuser_relations'
