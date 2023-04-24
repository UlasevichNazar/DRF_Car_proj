from rest_framework import serializers
from .models import Car, NewUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['username', 'user_telephone']


class CarSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # owner = UserSerializer(read_only=True)

    class Meta:
        model = Car
        fields = ["country", "car_brand", "car_model", "car_status", "car_year_of_issue", "car_condition", "car_color",
                  "car_price", "slug", 'owner']
        # fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = '__all__'

    def save(self, **kwargs):
        user = NewUser(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({password: "пароль не совпадает"})
        user.set_password(password)
        user.save()
        return user
