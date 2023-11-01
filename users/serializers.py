from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Переопределения методов для хеширования паролей"""
    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    def update(self, *args, **kwargs):
        user = super().update(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user
    class Meta:
        model = User
        fields = '__all__'