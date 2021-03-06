# Generated by Django 2.2.6 on 2019-11-04 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('item', models.CharField(max_length=200)),
                ('user_id', models.IntegerField()),
                ('is_ordered', models.BooleanField(default=False)),
                ('price', models.FloatField()),
            ],
        ),
    ]
