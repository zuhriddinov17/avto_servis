from main.models import *
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, GenericAPIView
from main.serializers import *


# """""Start CRUD Employee Model"""
# create model
class Create_Employee_Api_View(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
# end create model

# read model
class Get_All_Employee_Items(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
# end read model

# update model
class Update_Employee_Api_View(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
# end update model

# delete model
class Delete_Employee_Api_View(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
# end delete model
# """""End CRUD Employee Model"""

# """""Start CRUD Order Model"""
# create model
class Create_Order_Api_View(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
# end create model

# read model
class Get_All_Order_Items(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
# end read model

# update model
class Update_Order_Api_View(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
# end update model

# delete model
class Delete_Order_Api_View(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
# end delete model
# """""End CRUD Order Model"""

# """""Start CRUD Payment Model"""
# create model
class Create_Payment_Api_View(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
# end create model

# read model
class Get_All_Payment_Items(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
# end read model

# update model
class Update_Payment_Api_View(UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
# end update model

# delete model
class Delete_Payment_Api_View(DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
# end delete model
# """""End CRUD Payment Model"""




# """""Start CRUD Cassa Model"""
# create model
class Create_Cassa_Api_View(CreateAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializer
# end create model

# read model
class Get_All_Cassa_Items(ListAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializer
# end read model

# update model
class Update_Cassa_Api_View(UpdateAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializer
# end update model

# delete model
class Delete_Cassa_Api_View(DestroyAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializer
# end delete model
# """""End CRUD Cassa Model"""

# """""Start CRUD Garage Model"""
# create model
class Create_Garage_Api_View(CreateAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer
# end create model

# read model
class Get_All_Garage_Items(ListAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer
# end read model

# update model
class Update_Garage_Api_View(UpdateAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer
# end update model

# delete model
class Delete_Garage_Api_View(DestroyAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer
# end delete model
# """""End CRUD Garage Model"""


# """""Start CRUD Comment Model"""
# create model
class Create_Comment_Api_View(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
# end create model

# read model
class Get_All_Comment_Items(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
# end read model

# update model
class Update_Comment_Api_View(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
# end update model

# delete model
class Delete_Comment_Api_View(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
# end delete model
# """""End CRUD Comment Model"""
