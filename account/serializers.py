from rest_framework import serializers

from account.models import User


class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class UserWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password', 'email']

    def create(self, validated_data):
        password = validated_data.pop('password', None) # On retire le mot de passe des données validées
        instance = self.Meta.model(**validated_data) # On crée l'instance sans le mot de passe
        if password is not None:
            instance.set_password(password) # ICI : Django hache le mot de passe (PBKDF2 par défaut)
        instance.save()
        return instance
