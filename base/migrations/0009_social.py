# Generated by Django 5.0.2 on 2024-06-02 10:19

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_setting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('link', models.CharField(max_length=255, verbose_name='Link')),
                ('icon', models.FileField(upload_to='social_icons', verbose_name='Icon')),
                ('sort', models.IntegerField(default=0, verbose_name='Sort')),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Socials',
                'ordering': ['sort'],
            },
        ),
    ]
