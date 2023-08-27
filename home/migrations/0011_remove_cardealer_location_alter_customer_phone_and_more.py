# Generated by Django 4.2.4 on 2023-08-26 21:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_merge_20230827_0253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardealer',
            name='location',
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=11, validators=[django.core.validators.MinLengthValidator(11), django.core.validators.MaxLengthValidator(11)]),
        ),
        migrations.AddField(
            model_name='cardealer',
            name='location',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.location'),
        ),
    ]