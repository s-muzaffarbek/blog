from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import serializers
from django.conf import settings
from rest_framework.authtoken.models import Token
from account.models import MyUser

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input type': 'password'}, write_only=True)

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password', 'password2']

    def save(self, **kwargs):
        user = MyUser(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Password mos emas'})
        user.set_password(password)
        user.save()
        return user

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)