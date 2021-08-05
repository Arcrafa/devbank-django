from rest_framework import serializers

from interested import models

class InterestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Interested
        fields = '__all__'