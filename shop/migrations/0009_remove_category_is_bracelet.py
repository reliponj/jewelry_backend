# Generated by Django 5.0.2 on 2024-07-23 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_remove_category_is_constructor_category_is_bracelet_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='is_bracelet',
        ),
    ]