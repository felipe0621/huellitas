from rest_framework import serializers
from hueApp.models import MediosP, User
from .mediosPSerializers import MediosPSerializer

class UserSerializer(serializers.ModelSerializer):
    mediosP = MediosPSerializer()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'idCard', 'address', 'phone' 'email', 'mediosP']
        #'idCard', 'address', 'phone',
        
        
    def create(self, validated_data):
        mediosPData = validated_data.pop('mediosP')
        userInstance = User.objects.create(**validated_data)
        MediosP.objects.create(user=userInstance, **mediosPData)
        return userInstance
    
    def to_representation(self, obj):
      user = User.objects.get(id=obj.id)
      mediosP = MediosP.objects.get(user=obj.id)
      return{
          'id': user.id,
          'username': user.username,
          'name': user.name,
          'idCard': user.idCard,
          'address': user.address,
          'phone': user.phone,        
          'email': user.email,
          'mediosP': {
              'id': mediosP.id,
              'valorApagar': mediosP.valorApagar,
              'efectivo': mediosP.efectivo,
              'tarjeta_debito': mediosP.tarjeta_debito,
              'tarjeta_credito': mediosP.tarjeta_credito,
              'pse': mediosP.pse,
              'isActive': mediosP.isActive
          }          
      }  
