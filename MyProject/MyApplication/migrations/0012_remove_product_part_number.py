# Generated by Django 4.2.3 on 2023-08-22 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApplication', '0011_alter_product_recieved_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='part_number',
        ),
    ]
