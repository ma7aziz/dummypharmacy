# Generated by Django 3.0 on 2020-02-09 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_cart_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='session',
        ),
    ]
