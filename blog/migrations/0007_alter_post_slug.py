# Generated by Django 4.2.8 on 2023-12-31 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
    ]