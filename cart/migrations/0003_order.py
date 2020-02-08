# Generated by Django 3.0 on 2020-02-04 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0002_cart_qty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique_for_date=True)),
                ('total_price', models.FloatField()),
                ('shipping_address', models.CharField(blank=True, max_length=500)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.Cart')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
