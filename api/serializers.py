from rest_framework import serializers
from urlhandler import models as model

class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = model.Data
        fields = '__all__'