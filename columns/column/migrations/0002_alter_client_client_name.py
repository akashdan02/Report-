# Generated by Django 4.0.6 on 2022-08-05 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('column', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_name',
            field=models.CharField(max_length=200),
        ),
    ]
