# Generated by Django 4.2 on 2023-04-21 12:45

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(choices=[('m', 'мужской'), ('f', 'женский')], default='m', max_length=1, verbose_name='Пол')),
                ('birthday', models.DateField(default=datetime.date.today, null=True, verbose_name='Дата рождения')),
                ('user_telephone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Телефон')),
                ('profile_pic', models.ImageField(blank=True, default='images.png', upload_to='users_images/', verbose_name='Фотография')),
                ('status', models.CharField(blank=True, max_length=255, verbose_name='Статус')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CreditCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CardNumber', models.FloatField(verbose_name='Номер картоички')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.TextField(verbose_name='Страна')),
                ('car_brand', models.CharField(max_length=50, verbose_name='Марка')),
                ('car_model', models.CharField(max_length=100, verbose_name='Модель')),
                ('car_status', models.CharField(choices=[('in stock', 'В наличии'), ('out of stock', 'Не в наличии')], default='', max_length=20, verbose_name='Статус')),
                ('car_generation', models.CharField(blank=True, max_length=255, verbose_name='Поколение')),
                ('car_year_of_issue', models.DateField(blank=True, default=datetime.date.today, verbose_name='Год выпуска')),
                ('car_mileage', models.CharField(blank=True, default=0, verbose_name='Пробег')),
                ('car_color', models.CharField(blank=True, max_length=50, verbose_name='Цвет')),
                ('car_engine', models.CharField(blank=True, max_length=255, verbose_name='Двигатель')),
                ('car_complectation', models.CharField(blank=True, max_length=50, verbose_name='Комплектация')),
                ('car_drive_unit', models.CharField(blank=True, max_length=50, verbose_name='Привод')),
                ('car_steering_wheel', models.CharField(blank=True, max_length=25, verbose_name='Руль')),
                ('car_condition', models.CharField(blank=True, max_length=255, verbose_name='Состояние автомобиля')),
                ('car_owners', models.IntegerField(blank=True, default=1, verbose_name='Владельцы')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('car_price', models.FloatField(verbose_name='Цена')),
                ('owner_comments', models.TextField(default="It's my comment", verbose_name='Коментарии продавца')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фотография')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Машины',
                'verbose_name_plural': 'Машины',
                'ordering': ['id', 'country'],
            },
        ),
        migrations.AddField(
            model_name='newuser',
            name='user_credit_card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_web_site.creditcards', verbose_name='Кредитная карточка'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
