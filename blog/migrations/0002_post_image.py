# Generated by Django 4.2.8 on 2023-12-26 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
    ]
