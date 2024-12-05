from rest_framework import serializers
from usuarios.models import User
from usuarios.validators import validate_username, validate_cpf, validate_email, celular_invalido
from django.contrib.auth import authenticate

class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'phone_number']
    
    def validade(self,dados):
        if not validate_username(dados['username']):
            raise serializers.ValidationError('Username não pode conter caracteres especiais ou números.')
        
        if not validate_cpf(dados['cpf']):
            raise serializers.ValidationError('CPF inválido.')
        
        if not validate_email(dados['email']):
            raise serializers.ValidationError('Email inválido.')
        
        if celular_invalido(dados['phone_number']):
            raise serializers.ValidationError('Número de celular inválido.')
        
        return dados
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class LoginSerializers(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username = username, password = password)
        if not user:
            raise serializers.ValidationError('Credenciais inválidas.')
        data['user'] = user
        return data
    