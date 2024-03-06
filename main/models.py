from django.db import models
import qrcode.constants
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from .validators import ImageFileValidator
import qrcode
from io import BytesIO
from django.core.files import File



class User(AbstractUser):
    full_name = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, verbose_name='Parol', validators=[
        RegexValidator(
            regex='(?=^.{8}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.[A-Z])(?=.*[a-z]).*$',
            message='Invalid password number',
            code = 'password number'
        )
    ])
    phone_number = models.CharField(max_length=13, unique=True, verbose_name='Telefon raqamingizni kiriting',
                                    validators=[
                                        RegexValidator(
                                            regex='^[\+]9{2}8{1}[0-9]{9}$',
                                            message='Invalid phone number',
                                            code='invalid_number',
                                        )])
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Foydalanuvchilar'


class Employee(models.Model):
    user = models.OneToOneField(to='User', on_delete=models.CASCADE)
    profession = models.CharField(max_length=55)
    wages = models.PositiveIntegerField()
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    work_time = models.DateTimeField(default=0)
    rating = models.CharField(max_length=25)
    garage = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Xodimlar'


class Cassa(models.Model):
    summa = models.IntegerField()

    class Meta:
        verbose_name = 'cassa'
        verbose_name_plural = 'kassa'


class Payment(models.Model):
    order = models.CharField(max_length=55)
    code = models.CharField(max_length=25)
    payment = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    payment_type = models.CharField(max_length=255, choices=(
        (1, 'card'),
        (2, 'cash'),
        (3, 'other'),
    ))
    admin = models.ForeignKey(to='Employee', on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=3,
        )
        qr.add_date(f"Your data to encode in the QR code: {self.payment.order}")
        qr.make(fit=True)
        img = qr.image(fill_color="black", black_color="white")

        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'payment'
        verbose_name_plural = 'Tolovlar'


class Order(models.Model):
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=3,
        )
        qr.add_date(f"Your data to encode in the QR code: {self.order.owner_name}")
        qr.make(fit=True)
        img = qr.image(fill_color="black", black_color="white")

        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)


    owner_name = models.CharField(max_length=55)
    owner_phone_number = models.CharField(max_length=13, unique=True, verbose_name="Telefon raqam")
    is_delivery = models.BooleanField()
    address = models.CharField(max_length=255)
    car_name = models.CharField(max_length=25)
    car_number = models.CharField(max_length=25)
    is_active = models.CharField(max_length=255, choices=(
        (1, 'is_waiting'),
        (2, 'is_seeing'),
        (3, 'done'),
    ))
    master_employee_type = models.ForeignKey(to='Employee', on_delete=models.CASCADE)
    problem = models.CharField(max_length=55)
    service_cost = models.IntegerField()
    start_day = models.DateTimeField()
    start_time = models.TimeField(auto_now=True)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural= 'buyurtmalar'

class Garage(models.Model):
    name = models.CharField(max_length=55)
    garage_number = models.IntegerField()


    class Meta:
        verbose_name = 'Garage'
        verbose_name_plural = 'Garajlar'


class Comment(models.Model):
    type = models.CharField(max_length=55)
    text = models.TextField()
    created_at = models.CharField(max_length=55)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'kommentariyalar'


