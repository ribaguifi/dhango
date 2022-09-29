# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

DH_SCHEMA = "common"

class Inventory(models.Model):
    updated = models.DateTimeField()
    created = models.DateTimeField()
    id = models.CharField(primary_key=True, max_length=-1)
    name = models.TextField(unique=True)  # This field type is a guess.
    tag_provider = models.CharField(max_length=-1)
    tag_token = models.UUIDField(unique=True)
    org_id = models.UUIDField()

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"inventory'



class Manufacturer(models.Model):
    name = models.TextField(primary_key=True)  # This field type is a guess.
    url = models.CharField(unique=True, max_length=-1, blank=True, null=True)
    logo = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"manufacturer'


class Session(models.Model):
    updated = models.DateTimeField()
    created = models.DateTimeField()
    id = models.BigIntegerField(primary_key=True)
    expired = models.BigIntegerField(blank=True, null=True)
    token = models.UUIDField(unique=True)
    type = models.SmallIntegerField()
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"session'


class User(models.Model):
    updated = models.DateTimeField()
    created = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    email = models.CharField(unique=True, max_length=255)
    password = models.BinaryField(blank=True, null=True)
    token = models.UUIDField(unique=True)
    active = models.BooleanField()
    phantom = models.BooleanField()

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"user'


class UserInventory(models.Model):
    user = models.OneToOneField(User, models.DO_NOTHING, primary_key=True)
    inventory = models.ForeignKey(Inventory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"user_inventory'
        unique_together = (('user', 'inventory'),)
