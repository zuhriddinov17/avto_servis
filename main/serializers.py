from main.models import User, Employee, Order, Payment,  Cassa, Garage, Comment
from rest_framework import serializers


#""" The id is not displayed to hide the model number """

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'email', 'id', )


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('user', 'address', 'occupation', 'garage', 'experience', 'wages', 'start_work_time', 'end_work_time', 'day_off', 'queue', 'qr_code', )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('code', 'owner_name', 'owner_phone_number', 'owner_car_number', 'car_passport_number', 'id', )


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        exclude = ('code', 'id', )




class CassaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cassa
        fields = ('total_summa', )


class GarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = ('number', )



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('order', 'type', 'create_at', )


