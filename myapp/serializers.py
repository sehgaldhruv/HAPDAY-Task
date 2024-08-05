from rest_framework import serializers
from myapp.models import AppleHealthStat

class AppleHealthStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppleHealthStat
        fields = '__all__'
