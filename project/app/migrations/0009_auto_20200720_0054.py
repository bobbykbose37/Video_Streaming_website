# Generated by Django 3.0.8 on 2020-07-19 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_videoo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoo',
            name='videofile',
            field=models.FileField(null=True, upload_to='videos/'),
        ),
    ]
