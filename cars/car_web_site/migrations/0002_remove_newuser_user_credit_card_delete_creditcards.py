# Generated by Django 4.2 on 2023-04-21 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_web_site', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='user_credit_card',
        ),
        migrations.DeleteModel(
            name='CreditCards',
        ),
    ]
