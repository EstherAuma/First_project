# Generated by Django 4.2.3 on 2023-08-22 15:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MyApplication', '0012_remove_product_part_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='sale_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
