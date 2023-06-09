from rest_framework import serializers
from .models import User as MyUser
from .models import App, Task
class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App 
        fields = ('name',)  

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser 
        fields = ('username',) 
class TaskSerializer(serializers.ModelSerializer):
    apps = AppSerializer(many=True) 
    user = UserSerializer()
    class Meta:
        model = Task 
        fields = ('id', 'name', 'user', 'apps', 'is_completed') 
class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = MyUser
        fields = ['username',  'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = MyUser(username=self.validated_data['username'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(style={"input_type": "password"}, required=True)
    new_password = serializers.CharField(style={"input_type": "password"}, required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({'current_password': 'Does not match'})
        return value
