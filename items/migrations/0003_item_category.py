# Generated by Django 2.2.6 on 2019-11-01 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20191101_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('general', 'GENERAL'), ('supplments', 'SUPPLMENTS'), ('pain killers', 'PAIN KILLERS'), ('cold-cough', 'COLD-COUGH'), ('stomach', 'STOMACH'), ('skin-care', 'SKIN-CARE'), ('hair-care', 'HAIR_CARE')], default='general', max_length=25),
        ),
    ]
