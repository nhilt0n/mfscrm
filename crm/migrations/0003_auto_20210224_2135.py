# Generated by Django 3.1.7 on 2021-02-25 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_product_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='charge',
            new_name='p_charge',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='pickup_time',
            new_name='p_pickup_time',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product',
            new_name='p_product',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='quantity',
            new_name='p_quantity',
        ),
    ]
