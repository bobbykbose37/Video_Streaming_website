# Generated by Django 3.0.8 on 2020-07-17 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_releases'),
    ]

    operations = [
        migrations.CreateModel(
            name='discover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='discover')),
            ],
        ),
    ]