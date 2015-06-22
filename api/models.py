from django.db import models

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


# Create your models here.

class Wuser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    email = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
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

    @update_id
    def save(self):
        # Now actually save the object.
        super(Wuser, self).save()

    class Meta:
        managed = False
        db_table = 'wuser'


class WuserPhoto(models.Model):
    id = models.BigIntegerField(primary_key=True)
    wuser_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    photo_name = models.CharField(max_length=10, blank=True, null=True)
    time_created = models.DateTimeField(blank=True, null=True)
    is_deleted = models.NullBooleanField()
    is_profile_photo = models.NullBooleanField()
    time_updated = models.DateTimeField(blank=True, null=True)
    is_enabled = models.NullBooleanField()
    mask_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

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


class WuserProperties(models.Model):
    id = models.BigIntegerField(primary_key=True)
    wuser_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prop_type = models.CharField(max_length=10, blank=True, null=True)
    prop_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wuser_properties'

class WuserRelations(models.Model):
    id = models.BigIntegerField(primary_key=True)
    wuser_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    counterparty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    relation = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    wuser_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    counterparty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    chat_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    time_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wuser_chats'

class Events(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    venue = models.CharField(max_length=10, blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    time_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


class WuserEvents(models.Model):
    id = models.BigIntegerField(primary_key=True)
    wuser_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    event_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    time_created = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'wuser_events'

