# Generated by Django 3.2.6 on 2021-09-23 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_rename_product_orderlineitem_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='Product',
            new_name='product',
        ),
    ]
