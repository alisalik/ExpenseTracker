from rest_framework import serializers
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):

    uutoken=serializers.ReadOnlyField()
    class Meta:
        model = UserProfile
        fields = ['email','name','password','total_income','uutoken']
        extra_kwargs = {
            'password':
            {
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self,instance,validated_data):
        for attr,value in validated_data:
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance,attr,value)

        instance.save()
        return instance
