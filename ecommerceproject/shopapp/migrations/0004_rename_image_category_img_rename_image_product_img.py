# Generated by Django 4.0.5 on 2022-07-05 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0003_alter_product_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='image',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='img',
        ),
    ]