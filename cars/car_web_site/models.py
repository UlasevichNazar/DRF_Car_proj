from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
import datetime
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from cars import settings


class Car(models.Model):
    CAR_STATUS = (
        ("in stock", "В наличии"),
        ("out of stock", "Не в наличии")
    )
    country = models.TextField(blank=False, verbose_name='Страна')
    car_brand = models.CharField(max_length=50, verbose_name='Марка')
    car_model = models.CharField(max_length=100, verbose_name='Модель')
    car_status = models.CharField(max_length=20, choices=CAR_STATUS, default='', verbose_name="Статус")
    car_generation = models.CharField(max_length=255, blank=True, verbose_name="Поколение")
    car_year_of_issue = models.DateField(default=datetime.date.today, blank=True,
                                         verbose_name="Год выпуска")
    car_mileage = models.CharField(blank=True, default=0, verbose_name="Пробег")
    car_color = models.CharField(max_length=50, blank=True, verbose_name="Цвет")
    car_engine = models.CharField(max_length=255, blank=True, verbose_name="Двигатель")
    car_complectation = models.CharField(max_length=50, blank=True, verbose_name="Комплектация")
    car_drive_unit = models.CharField(max_length=50, blank=True, verbose_name="Привод")
    car_steering_wheel = models.CharField(max_length=25, blank=True, verbose_name="Руль")
    car_condition = models.CharField(max_length=255, blank=True, verbose_name="Состояние автомобиля")
    car_owners = models.IntegerField(blank=True, null=False,default=1, verbose_name="Владельцы")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    car_price = models.FloatField(blank=False, verbose_name='Цена')
    owner_comments = models.TextField(blank=False, default="It's my comment", verbose_name='Коментарии продавца')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фотография", blank=True, default="images.png")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец")

    def __str__(self):
        return f'{self.car_brand} ( {self.car_model} )'

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Машины"
        verbose_name_plural = "Машины"
        ordering = ['id', 'country']






class NewUser(AbstractUser):
    GENDERS = (
        ("m", "мужской"),
        ("f", "женский")
    )

    gender = models.CharField("Пол", max_length=1, choices=GENDERS, default='m')
    birthday = models.DateField("Дата рождения", default=datetime.date.today, null=True)
    user_telephone = PhoneNumberField(unique=False, blank=True, verbose_name="Телефон", null=True)
    profile_pic = models.ImageField(upload_to="users_images/", verbose_name="Фотография", blank=True,
                                    default="images.png")
    status = models.CharField("Статус", max_length=255, blank=True)
