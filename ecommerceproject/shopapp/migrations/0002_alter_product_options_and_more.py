# Generated by Django 4.0.5 on 2022-07-04 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': ('product',), 'verbose_name_plural': ('products',)},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='caregory',
            new_name='category',
        ),
    ]
