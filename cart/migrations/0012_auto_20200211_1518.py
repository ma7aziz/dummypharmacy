# Generated by Django 3.0 on 2020-02-11 13:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20191104_2156'),
        ('cart', '0011_remove_cart_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='qty',
        ),
        migrations.AddField(
            model_name='cart',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='cart',
            name='item',
        ),
        migrations.CreateModel(
            name='Order_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Item')),
                ('shopping_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Cart')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ManyToManyField(to='cart.Order_item'),
        ),
    ]