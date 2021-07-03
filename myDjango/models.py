# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SetFeatures(models.Model):
    test_id = models.IntegerField(primary_key=True)
    h1n1_concern = models.IntegerField(blank=True, null=True)
    h1n1_knowledge = models.IntegerField(blank=True, null=True)
    behavioral_antiviral_meds = models.IntegerField(blank=True, null=True)
    behavioral_avoidance = models.IntegerField(blank=True, null=True)
    behavioral_face_mask = models.IntegerField(blank=True, null=True)
    behavioral_wash_hands = models.IntegerField(blank=True, null=True)
    behavioral_large_gatherings = models.IntegerField(blank=True, null=True)
    behavioral_outside_home = models.IntegerField(blank=True, null=True)
    behavioral_touch_face = models.IntegerField(blank=True, null=True)
    doctor_recc_h1n1 = models.IntegerField(blank=True, null=True)
    doctor_recc_seasonal = models.IntegerField(blank=True, null=True)
    chronic_med_condition = models.IntegerField(blank=True, null=True)
    child_under_6_months = models.IntegerField(blank=True, null=True)
    health_worker = models.IntegerField(blank=True, null=True)
    health_insurance = models.IntegerField(blank=True, null=True)
    opinion_h1n1_vacc_effective = models.IntegerField(blank=True, null=True)
    opinion_h1n1_risk = models.IntegerField(blank=True, null=True)
    opinion_h1n1_sick_from_vacc = models.IntegerField(blank=True, null=True)
    opinion_seas_vacc_effective = models.IntegerField(blank=True, null=True)
    opinion_seas_risk = models.IntegerField(blank=True, null=True)
    opinion_seas_sick_from_vacc = models.IntegerField(blank=True, null=True)
    age_group = models.CharField(max_length=30, blank=True, null=True)
    education = models.CharField(max_length=30, blank=True, null=True)
    race = models.CharField(max_length=30, blank=True, null=True)
    sex = models.CharField(max_length=30, blank=True, null=True)
    income_poverty = models.CharField(max_length=30, blank=True, null=True)
    marital_status = models.CharField(max_length=30, blank=True, null=True)
    rent_or_own = models.CharField(max_length=30, blank=True, null=True)
    employment_status = models.CharField(max_length=30, blank=True, null=True)
    hhs_geo_region = models.CharField(max_length=30, blank=True, null=True)
    census_msa = models.CharField(max_length=30, blank=True, null=True)
    household_adults = models.IntegerField(blank=True, null=True)
    household_children = models.IntegerField(blank=True, null=True)
    employment_industry = models.CharField(max_length=30, blank=True, null=True)
    employment_occupation = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'set_features'


class SetLabels(models.Model):
    label_id = models.IntegerField(primary_key=True)
    h1n1_vaccine = models.IntegerField(blank=True, null=True)
    seasonal_vaccine = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'set_labels'


class TestLabel(models.Model):
    test = models.OneToOneField(SetFeatures, models.DO_NOTHING, primary_key=True)
    label = models.ForeignKey(SetLabels, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'test_label'
        unique_together = (('test', 'label'),)
