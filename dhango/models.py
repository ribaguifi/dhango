# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# TODO @slamora: copy of ereuse_devicehub.resources.models.py
STR_XSM_SIZE = 16
STR_SM_SIZE = 32
STR_SIZE = 64
STR_BIG_SIZE = 128

# TODO load from settings or .env
# from django.conf import settings
DH_SCHEMA = "dbtest"


class Action(models.Model):
    updated = models.DateTimeField()
    created = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    type = models.CharField(max_length=STR_SIZE)
    name = models.TextField()  # This field type is a guess.
    severity = models.SmallIntegerField()
    closed = models.BooleanField()
    description = models.TextField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    snapshot = models.ForeignKey('Snapshot', models.DO_NOTHING, blank=True, null=True)
    author_id = models.UUIDField()
    agent = models.ForeignKey('Agent', models.DO_NOTHING)
    parent = models.ForeignKey('Computer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"action'


class ActionComponent(models.Model):
    device = models.OneToOneField('Component', models.DO_NOTHING, primary_key=True)
    action = models.ForeignKey(Action, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"action_component'
        unique_together = (('device', 'action'),)


class ActionDevice(models.Model):
    device = models.OneToOneField('Device', models.DO_NOTHING, primary_key=True)
    action = models.ForeignKey(Action, models.DO_NOTHING)
    created = models.DateTimeField()
    author_id = models.UUIDField()

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"action_device'
        unique_together = (('device', 'action'),)


class ActionStatus(models.Model):
    rol_user_id = models.UUIDField()
    trade = models.ForeignKey('Trade', models.DO_NOTHING, blank=True, null=True)
    id = models.OneToOneField(Action, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"action_status'


class ActionStatusDocuments(models.Model):
    rol_user_id = models.UUIDField()
    id = models.OneToOneField(Action, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"action_status_documents'


class ActionTradeDocument(models.Model):
    document = models.OneToOneField('TradeDocument', models.DO_NOTHING, primary_key=True)
    action = models.ForeignKey(Action, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"action_trade_document'
        unique_together = (('document', 'action'),)


class ActionWithOneDevice(models.Model):
    device = models.ForeignKey('Device', models.DO_NOTHING)
    id = models.OneToOneField(Action, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"action_with_one_device'


class Agent(models.Model):
    updated = models.DateTimeField()
    created = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    type = models.CharField(max_length=STR_SIZE)
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    tax_id = models.CharField(max_length=32, blank=True, null=True)
    country = models.TextField(blank=True, null=True)  # This field type is a guess.
    telephone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"agent'
        unique_together = (('tax_id', 'name'), ('tax_id', 'country'),)


class Allocate(models.Model):
    final_user_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    transaction = models.TextField(blank=True, null=True)  # This field type is a guess.
    end_users = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    id = models.OneToOneField(Action, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"allocate'


class Battery(models.Model):
    wireless = models.BooleanField(blank=True, null=True)
    technology = models.TextField(blank=True, null=True)  # This field type is a guess.
    size = models.IntegerField()
    id = models.OneToOneField('Component', models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"battery'


class Benchmark(models.Model):
    elapsed = models.DurationField(blank=True, null=True)
    id = models.OneToOneField(ActionWithOneDevice, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"benchmark'


class BenchmarkDataStorage(models.Model):
    id = models.OneToOneField(Benchmark, models.DO_NOTHING, db_column='id', primary_key=True)
    read_speed = models.FloatField()
    write_speed = models.FloatField()

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"benchmark_data_storage'


class BenchmarkWithRate(models.Model):
    id = models.OneToOneField(Benchmark, models.DO_NOTHING, db_column='id', primary_key=True)
    rate = models.FloatField()

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"benchmark_with_rate'


class Component(models.Model):
    id = models.OneToOneField('Device', models.DO_NOTHING, db_column='id', primary_key=True)
    parent = models.ForeignKey('Computer', models.DO_NOTHING, blank=True, null=True)
    focal_length = models.SmallIntegerField(blank=True, null=True)
    video_height = models.SmallIntegerField(blank=True, null=True)
    video_width = models.IntegerField(blank=True, null=True)
    horizontal_view_angle = models.IntegerField(blank=True, null=True)
    facing = models.TextField(blank=True, null=True)  # This field type is a guess.
    vertical_view_angle = models.SmallIntegerField(blank=True, null=True)
    video_stabilization = models.BooleanField(blank=True, null=True)
    flash = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"component'


class Computer(models.Model):
    id = models.OneToOneField('Device', models.DO_NOTHING, db_column='id', primary_key=True)
    chassis = models.TextField(blank=True, null=True)  # This field type is a guess.
    amount = models.IntegerField(blank=True, null=True)
    owner_id = models.UUIDField()
    transfer_state = models.SmallIntegerField()
    receiver_id = models.UUIDField(blank=True, null=True)
    layout = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"computer'


class ComputerAccessory(models.Model):
    id = models.OneToOneField('Device', models.DO_NOTHING, db_column='id', primary_key=True)
    layout = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"computer_accessory'


class Confirm(models.Model):
    user_id = models.UUIDField()
    action = models.ForeignKey(Action, models.DO_NOTHING)
    # id = models.OneToOneField(Action, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"confirm'


class ConfirmDocument(models.Model):
    user_id = models.UUIDField()
    action = models.ForeignKey(Action, models.DO_NOTHING)
    # id = models.OneToOneField(Action, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"confirm_document'


class DataStorage(models.Model):
    size = models.IntegerField(blank=True, null=True)
    interface = models.TextField(blank=True, null=True)  # This field type is a guess.
    id = models.OneToOneField(Component, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"data_storage'


class DataWipe(models.Model):
    document = models.ForeignKey('DataWipeDocument', models.DO_NOTHING)
    id = models.OneToOneField(Action, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"data_wipe'


class DataWipeDocument(models.Model):
    software = models.TextField(blank=True, null=True)  # This field type is a guess.
    success = models.BooleanField(blank=True, null=True)
    id = models.OneToOneField('Document', models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"data_wipe_document'


class Deallocate(models.Model):
    transaction = models.TextField(blank=True, null=True)  # This field type is a guess.
    id = models.OneToOneField(Action, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"deallocate'


class Deliverynote(models.Model):
    updated = models.DateTimeField()
    created = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    document_id = models.TextField()  # This field type is a guess.
    creator_id = models.UUIDField()
    supplier_email = models.TextField()  # This field type is a guess.
    receiver_address = models.TextField()  # This field type is a guess.
    date = models.DateTimeField()
    amount = models.IntegerField(blank=True, null=True)
    expected_devices = models.JSONField()
    transferred_devices = models.TextField(blank=True, null=True)  # This field type is a guess.
    transfer_state = models.SmallIntegerField()
    lot = models.ForeignKey('Lot', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"deliverynote'


class Device(models.Model):
    updated = models.DateTimeField()
    created = models.DateTimeField()
    id = models.BigIntegerField(primary_key=True)
    type = models.CharField(max_length=32)
    hid = models.CharField(max_length=STR_SIZE, blank=True, null=True)
    model = models.CharField(max_length=STR_SIZE, blank=True, null=True)
    manufacturer = models.CharField(max_length=STR_SIZE, blank=True, null=True)
    serial_number = models.CharField(max_length=STR_SIZE, blank=True, null=True)
    brand = models.TextField(blank=True, null=True)  # This field type is a guess.
    generation = models.SmallIntegerField(blank=True, null=True)
    version = models.TextField(blank=True, null=True)  # This field type is a guess.
    weight = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    production_date = models.DateTimeField(blank=True, null=True)
    variant = models.TextField(blank=True, null=True)  # This field type is a guess.
    sku = models.TextField(blank=True, null=True)  # This field type is a guess.
    image = models.CharField(max_length=STR_SIZE, blank=True, null=True)
    owner_id = models.UUIDField()
    allocated = models.BooleanField(blank=True, null=True)
    devicehub_id = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.
    active = models.BooleanField(blank=True, null=True)
    max_drill_bit_size = models.SmallIntegerField(blank=True, null=True)
    size = models.SmallIntegerField(blank=True, null=True)
    max_allowed_weight = models.IntegerField(blank=True, null=True)
    wheel_size = models.SmallIntegerField(blank=True, null=True)
    gears = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"device'


class DeviceSearch(models.Model):
    device = models.OneToOneField(Device, models.DO_NOTHING, primary_key=True)
    properties = models.TextField()  # This field type is a guess.
    tags = models.TextField(blank=True, null=True)  # This field type is a guess.
    devicehub_ids = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"device_search'


class Display(models.Model):
    size = models.FloatField(blank=True, null=True)
    technology = models.TextField(blank=True, null=True)  # This field type is a guess.
    resolution_width = models.SmallIntegerField(blank=True, null=True)
    resolution_height = models.SmallIntegerField(blank=True, null=True)
    refresh_rate = models.SmallIntegerField(blank=True, null=True)
    contrast_ratio = models.SmallIntegerField(blank=True, null=True)
    touchable = models.BooleanField(blank=True, null=True)
    id = models.OneToOneField(Component, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"display'


class Document(models.Model):
    updated = models.DateTimeField()
    created = models.DateTimeField()
    id = models.BigIntegerField(primary_key=True)
    document_type = models.CharField(max_length=32)
    date = models.DateTimeField(blank=True, null=True)
    id_document = models.TextField(blank=True, null=True)  # This field type is a guess.
    owner_id = models.UUIDField()
    file_name = models.TextField()  # This field type is a guess.
    file_hash = models.TextField()  # This field type is a guess.
    url = models.CharField(max_length=STR_SIZE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"document'


class EraseBasic(models.Model):
    id = models.OneToOneField(ActionWithOneDevice, models.DO_NOTHING, db_column='id', primary_key=True)
    method = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"erase_basic'


class GraphicCard(models.Model):
    memory = models.SmallIntegerField(blank=True, null=True)
    id = models.OneToOneField(Component, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"graphic_card'


class Individual(models.Model):
    active_org = models.ForeignKey('Organization', models.DO_NOTHING, blank=True, null=True)
    user_id = models.UUIDField(unique=True, blank=True, null=True)
    id = models.OneToOneField(Agent, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"individual'


class Install(models.Model):
    elapsed = models.DurationField()
    address = models.SmallIntegerField(blank=True, null=True)
    id = models.OneToOneField(ActionWithOneDevice, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"install'


class Live(models.Model):
    serial_number = models.CharField(max_length=STR_SIZE, blank=True, null=True)
    usage_time_hdd = models.DurationField(blank=True, null=True)
    snapshot_uuid = models.UUIDField(blank=True, null=True)
    software = models.TextField()  # This field type is a guess.
    software_version = models.CharField(max_length=32)
    licence_version = models.CharField(max_length=32)
    id = models.OneToOneField(ActionWithOneDevice, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"live'


class Lot(models.Model):
    updated = models.DateTimeField()
    created = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    name = models.TextField()  # This field type is a guess.
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    closed = models.BooleanField()
    amount = models.IntegerField(blank=True, null=True)
    owner_id = models.UUIDField()
    transfer_state = models.SmallIntegerField()
    receiver_address = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"lot'


class LotDevice(models.Model):
    device = models.OneToOneField(Device, models.DO_NOTHING, primary_key=True)
    lot = models.ForeignKey(Lot, models.DO_NOTHING)
    created = models.DateTimeField()
    author_id = models.UUIDField()

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"lot_device'
        unique_together = (('device', 'lot'),)


class MeasureBattery(models.Model):
    size = models.IntegerField()
    voltage = models.IntegerField()
    cycle_count = models.IntegerField(blank=True, null=True)
    health = models.TextField(blank=True, null=True)  # This field type is a guess.
    id = models.OneToOneField('Test', models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"measure_battery'


class Membership(models.Model):
    updated = models.DateTimeField()
    created = models.DateTimeField()
    id = models.CharField(max_length=STR_SIZE, blank=True, null=True)
    organization = models.OneToOneField('Organization', models.DO_NOTHING, primary_key=True)
    individual = models.ForeignKey(Individual, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"membership'
        unique_together = (('id', 'organization'), ('organization', 'individual'),)


class Migrate(models.Model):
    other = models.CharField(max_length=STR_SIZE)
    id = models.OneToOneField(Action, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"migrate'


class Mobile(models.Model):
    id = models.OneToOneField(Device, models.DO_NOTHING, db_column='id', primary_key=True)
    imei = models.BigIntegerField(blank=True, null=True)
    meid = models.CharField(max_length=STR_SIZE, blank=True, null=True)
    ram_size = models.IntegerField(blank=True, null=True)
    data_storage_size = models.IntegerField(blank=True, null=True)
    display_size = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"mobile'


class Monitor(models.Model):
    size = models.FloatField(blank=True, null=True)
    technology = models.TextField(blank=True, null=True)  # This field type is a guess.
    resolution_width = models.SmallIntegerField(blank=True, null=True)
    resolution_height = models.SmallIntegerField(blank=True, null=True)
    refresh_rate = models.SmallIntegerField(blank=True, null=True)
    contrast_ratio = models.SmallIntegerField(blank=True, null=True)
    touchable = models.BooleanField(blank=True, null=True)
    id = models.OneToOneField(Device, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"monitor'


class Motherboard(models.Model):
    slots = models.SmallIntegerField(blank=True, null=True)
    usb = models.SmallIntegerField(blank=True, null=True)
    firewire = models.SmallIntegerField(blank=True, null=True)
    serial = models.SmallIntegerField(blank=True, null=True)
    pcmcia = models.SmallIntegerField(blank=True, null=True)
    bios_date = models.DateField(blank=True, null=True)
    ram_slots = models.SmallIntegerField(blank=True, null=True)
    ram_max_size = models.IntegerField(blank=True, null=True)
    id = models.OneToOneField(Component, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"motherboard'


class MoveOnDocument(models.Model):
    weight = models.FloatField(blank=True, null=True)
    container_from = models.ForeignKey('TradeDocument', models.DO_NOTHING, related_name="moveondocument_from")
    container_to = models.ForeignKey('TradeDocument', models.DO_NOTHING, related_name="moveondocument_to")
    # id = models.OneToOneField(Action, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"move_on_document'


class NetworkAdapter(models.Model):
    speed = models.SmallIntegerField(blank=True, null=True)
    wireless = models.BooleanField()
    id = models.OneToOneField(Component, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"network_adapter'


class Networking(models.Model):
    speed = models.SmallIntegerField(blank=True, null=True)
    wireless = models.BooleanField()
    id = models.OneToOneField(Device, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"networking'


class Organization(models.Model):
    id = models.OneToOneField(Agent, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"organization'


class Organize(models.Model):
    id = models.OneToOneField(Action, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"organize'


class Path(models.Model):
    id = models.UUIDField(primary_key=True)
    lot = models.ForeignKey(Lot, models.DO_NOTHING)
    path = models.TextField(unique=True)  # This field type is a guess.
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"path'


class Price(models.Model):
    currency = models.TextField()  # This field type is a guess.
    price = models.DecimalField(max_digits=19, decimal_places=4)
    software = models.TextField(blank=True, null=True)  # This field type is a guess.
    version = models.CharField(max_length=STR_SIZE, blank=True, null=True)
    rating = models.ForeignKey('Rate', models.DO_NOTHING, blank=True, null=True)
    id = models.OneToOneField(ActionWithOneDevice, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"price'


class Printer(models.Model):
    id = models.OneToOneField(Device, models.DO_NOTHING, db_column='id', primary_key=True)
    wireless = models.BooleanField()
    scanning = models.BooleanField()
    technology = models.TextField(blank=True, null=True)  # This field type is a guess.
    monochrome = models.BooleanField()

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"printer'


class Processor(models.Model):
    speed = models.FloatField(blank=True, null=True)
    cores = models.SmallIntegerField(blank=True, null=True)
    threads = models.SmallIntegerField(blank=True, null=True)
    address = models.SmallIntegerField(blank=True, null=True)
    abi = models.CharField(max_length=STR_SIZE, blank=True, null=True)
    id = models.OneToOneField(Component, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"processor'


class RamModule(models.Model):
    size = models.SmallIntegerField(blank=True, null=True)
    speed = models.SmallIntegerField(blank=True, null=True)
    interface = models.TextField(blank=True, null=True)  # This field type is a guess.
    format = models.TextField(blank=True, null=True)  # This field type is a guess.
    id = models.OneToOneField(Component, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"ram_module'


class Rate(models.Model):
    rating = models.FloatField(blank=True, null=True)
    version = models.CharField(max_length=STR_SIZE, blank=True, null=True)
    appearance = models.FloatField(blank=True, null=True)
    functionality = models.FloatField(blank=True, null=True)
    id = models.OneToOneField(ActionWithOneDevice, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"rate'


class RateComputer(models.Model):
    processor = models.FloatField(blank=True, null=True)
    ram = models.FloatField(blank=True, null=True)
    data_storage = models.FloatField(blank=True, null=True)
    graphic_card = models.FloatField(blank=True, null=True)
    id = models.OneToOneField(Rate, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"rate_computer'


class ReportHash(models.Model):
    id = models.UUIDField(primary_key=True)
    created = models.DateTimeField()
    hash3 = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"report_hash'


class Snapshot(models.Model):
    uuid = models.UUIDField(unique=True, blank=True, null=True)
    version = models.CharField(max_length=32)
    software = models.TextField()  # This field type is a guess.
    elapsed = models.DurationField(blank=True, null=True)
    id = models.OneToOneField(ActionWithOneDevice, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"snapshot'


class SnapshotRequest(models.Model):
    id = models.OneToOneField(Snapshot, models.DO_NOTHING, db_column='id', primary_key=True)
    request = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"snapshot_request'


class SoundCard(models.Model):
    id = models.OneToOneField(Component, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"sound_card'


class Step(models.Model):
    erasure = models.OneToOneField(EraseBasic, models.DO_NOTHING, primary_key=True)
    type = models.CharField(max_length=32)
    num = models.SmallIntegerField()
    severity = models.SmallIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"step'
        unique_together = (('erasure', 'num'),)


class StressTest(models.Model):
    elapsed = models.DurationField()
    id = models.OneToOneField('Test', models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"stress_test'


class Tag(models.Model):
    updated = models.DateTimeField()
    created = models.DateTimeField()
    internal_id = models.BigIntegerField(unique=True)
    id = models.TextField(primary_key=True)  # This field type is a guess.
    owner_id = models.UUIDField()
    org = models.ForeignKey(Organization, models.DO_NOTHING, blank=True, null=True)
    provider = models.CharField(max_length=STR_SIZE, blank=True, null=True)
    device = models.ForeignKey(Device, models.DO_NOTHING, blank=True, null=True)
    secondary = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"tag'
        unique_together = (('secondary', 'owner_id'), ('id', 'owner_id'),)


class Test(models.Model):
    id = models.OneToOneField(ActionWithOneDevice, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"test'


class TestAudio(models.Model):
    speaker = models.BooleanField(blank=True, null=True)
    microphone = models.BooleanField(blank=True, null=True)
    id = models.OneToOneField(Test, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"test_audio'


class TestBios(models.Model):
    beeps_power_on = models.BooleanField(blank=True, null=True)
    access_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    id = models.OneToOneField(Test, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"test_bios'


class TestCamera(models.Model):
    id = models.OneToOneField(Test, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"test_camera'


class TestConnectivity(models.Model):
    id = models.OneToOneField(Test, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"test_connectivity'


class TestDataStorage(models.Model):
    length = models.TextField()  # This field type is a guess.
    status = models.CharField(max_length=STR_SIZE)
    lifetime = models.DurationField(blank=True, null=True)
    assessment = models.BooleanField(blank=True, null=True)
    reallocated_sector_count = models.BigIntegerField(blank=True, null=True)
    power_cycle_count = models.IntegerField(blank=True, null=True)
    reported_uncorrectable_errors = models.BigIntegerField(blank=True, null=True)
    command_timeout = models.BigIntegerField(blank=True, null=True)
    current_pending_sector_count = models.BigIntegerField(blank=True, null=True)
    offline_uncorrectable = models.BigIntegerField(blank=True, null=True)
    remaining_lifetime_percentage = models.SmallIntegerField(blank=True, null=True)
    elapsed = models.DurationField()
    id = models.OneToOneField(Test, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"test_data_storage'


class TestDisplayHinge(models.Model):
    id = models.OneToOneField(Test, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"test_display_hinge'


class TestKeyboard(models.Model):
    id = models.OneToOneField(Test, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"test_keyboard'


class TestPowerAdapter(models.Model):
    id = models.OneToOneField(Test, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"test_power_adapter'


class TestTrackpad(models.Model):
    id = models.OneToOneField(Test, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"test_trackpad'


class Trade(models.Model):
    user_from_id = models.UUIDField()
    user_to_id = models.UUIDField()
    price = models.FloatField(blank=True, null=True)
    currency = models.TextField()  # This field type is a guess.
    date = models.DateTimeField(blank=True, null=True)
    confirm = models.BooleanField()
    code = models.TextField(blank=True, null=True)  # This field type is a guess.
    lot = models.ForeignKey(Lot, models.DO_NOTHING, blank=True, null=True)
    id = models.OneToOneField(Action, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"trade'


class TradeDocument(models.Model):
    updated = models.DateTimeField()
    created = models.DateTimeField()
    id = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    id_document = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    owner_id = models.UUIDField()
    lot = models.ForeignKey(Lot, models.DO_NOTHING)
    file_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    file_hash = models.TextField(blank=True, null=True)  # This field type is a guess.
    url = models.CharField(max_length=STR_SIZE, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"trade_document'


class VisualTest(models.Model):
    appearance_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    functionality_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    labelling = models.BooleanField(blank=True, null=True)
    id = models.OneToOneField(Test, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = f'{DH_SCHEMA}\".\"visual_test'
