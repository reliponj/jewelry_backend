# Generated by Django 5.0.2 on 2024-05-26 20:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('phone_label', models.CharField(max_length=100, verbose_name='Phone Label')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('worktime', models.TextField(verbose_name='Worktime (next line ;)')),
                ('breaktime', models.TextField(verbose_name='Breaktime (next line ;)')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('slug', models.CharField(max_length=50, verbose_name='Slug')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('meta_title', models.CharField(max_length=50, verbose_name='Meta Title')),
                ('meta_text', models.TextField(verbose_name='Meta Text')),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
        ),
    ]
