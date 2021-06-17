from rest_framework import serializers
from .models import Applicant

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Applicant
        fields = ('subid', 'name_ins', 'eff_date', 'lob')