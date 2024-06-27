# Generated by Django 5.0.2 on 2024-06-26 12:13

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_constructor',
            field=models.BooleanField(default=False, verbose_name='Constructor?'),
        ),
        migrations.CreateModel(
            name='Bracelet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('products', models.ManyToManyField(blank=True, to='shop.product')),
            ],
            options={
                'verbose_name': 'Bracelet',
                'verbose_name_plural': 'Bracelets',
            },
        ),
    ]
