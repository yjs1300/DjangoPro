from django.db import models

# Create your models here.
class Member(models.Model):
    m_name = models.CharField(max_length=100)
    m_id = models.CharField(unique=True, max_length=100)
    m_pwd = models.CharField(max_length=100)
    m_email = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member'


class MemberHist(models.Model):
    fk_m = models.ForeignKey(Member, models.DO_NOTHING, to_field='m_id', blank=True, null=True)
    addr = models.CharField(max_length=255, blank=True, null=True)
    bike_load = models.CharField(max_length=100, blank=True, null=True)
    transport = models.CharField(max_length=100, blank=True, null=True)
    park = models.CharField(max_length=100, blank=True, null=True)
    tour = models.CharField(max_length=100, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    pred = models.CharField(max_length=100, blank=True, null=True)
    reg_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_hist'