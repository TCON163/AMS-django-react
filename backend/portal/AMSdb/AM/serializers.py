from rest_framework import serializers
from .models import Applicant

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ('subid', 'name_ins', 'lob', 'eff_date')