from django.db import models
from django.utils.translation import gettext as _
from datetime import date
# Create your models here.
class Applicant(models.Model):
    subid = models.BigAutoField(primary_key=True)
    name_ins = models.CharField(max_length=300)
    dba_name = models.CharField(max_length=300, blank=True)
    m_street_addy = models.CharField(max_length=120)
    m_street_2_addy = models.CharField(max_length=80, blank=True)
    m_city = models.CharField(max_length=35)
    m_zip = models.IntegerField()
    m_state = models.CharField(max_length=2)
    p_street_addy = models.CharField(max_length=120)
    p_street_2_addy = models.CharField(max_length=80, blank=True)
    p_city = models.CharField(max_length=35)
    p_zip = models.IntegerField()
    p_state = models.CharField(max_length=2)
    eff_date = models.DateField(default=date.today)
    lob = models.CharField(max_length=40)
    policy_num = models.CharField(max_length=50, blank=True)

    