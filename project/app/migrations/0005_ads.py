# Generated by Django 3.0.8 on 2020-07-18 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_features'),
    ]

    operations = [
        migrations.CreateModel(
            name='ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad1', models.ImageField(blank=True, upload_to='ads')),
                ('ad2', models.ImageField(blank=True, upload_to='ads')),
            ],
        ),
    ]
