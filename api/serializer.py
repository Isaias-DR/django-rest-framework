from rest_framework import serializers
from .models import Programmer


class ProgramerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        # fields = ('fullname', 'nickname')
        fields = '__all__'  # todos incluido el id que no esta  en el modelo y django lo crea
