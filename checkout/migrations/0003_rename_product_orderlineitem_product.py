# Generated by Django 3.2.6 on 2021-09-23 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20210923_2034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='product',
            new_name='Product',
        ),
    ]
