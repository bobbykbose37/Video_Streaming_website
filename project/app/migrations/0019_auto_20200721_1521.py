# Generated by Django 3.0.8 on 2020-07-21 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20200720_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='ad',
            field=models.FileField(blank=True, upload_to='addd'),
        ),
    ]
