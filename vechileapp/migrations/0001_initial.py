# Generated by Django 4.1.4 on 2023-05-10 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=250)),
                ('model', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
        ),
    ]
