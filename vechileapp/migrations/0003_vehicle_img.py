# Generated by Django 4.1.4 on 2023-05-11 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vechileapp', '0002_alter_vehicle_number_alter_vehicle_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='img',
            field=models.ImageField(default='gallery', upload_to='pics'),
        ),
    ]
