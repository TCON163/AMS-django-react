from django.contrib import admin
from .models import Applicant

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('subid', 'name_ins', 'eff_date', 'lob')

# Register your models here.

admin.site.register(Applicant, ApplicantAdmin)