# Generated by Django 5.0.2 on 2024-06-27 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_category_is_constructor_bracelet'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_for_bracelet',
            field=models.ImageField(blank=True, null=True, upload_to='bracelet_images', verbose_name='Bracelet image'),
        ),
    ]