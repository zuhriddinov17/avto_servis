from django.urls import path
from .views import *


urlpatterns = [
    #----------- filter employee urls --------------
    path('get-employee-garaj/', filter_employee_garaj),
    path('get-employee-rating/', filter_employee_rating),
    path('get-employee-address/', filter_employee_address),
    path('get-employee-exerience/', filter_employee_experience),
    path('get-employee-profession/', filter_employee_profession),
    path('get-employee-profession/', filter_employee_work_time),

    #----------------- filter order urls ------------

    path('get-order-owner-phone_number/', filter_order_owner_phone_number),
    path('get-order-owner-name/', filter_order_owner_name),
    path('get-order-address/', filter_order_address),
    path('get-order-car_name/', filter_order_car_name),
    path('get-order-problem/', filter_order_problem),
    path('get-order-start_day/', filter_order_start_day),
    path('get-order-employee/', filter_order_employee),
    path('get-order-employee/', filter_order_employee),

    #---------------- filter payment urls----------

    path('get-payment-order/', filter_payment_order),
    path('get-payment-code/', filter_payment_code),
    path('get-payment-created_at', filter_payment_created_at),
    path('get-paymentdate/', filter_payment_date),
    path('get-payment-payent_type/', filter_payment_payment_type),
    path('get-payment-admin/', filter_payment_admin),

    #----------------- filter report urls---------

    path('get-report-start-date/', filter_order_start_day),
    path('get-report-end_date/', filter_payment_date),
    path('get-report-employee/', filter_order_employee),

    #---------------- filter garag urls---------

    path('get-garaj-name/', filter_garaj_name)
]
