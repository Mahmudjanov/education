# Generated by Django 4.2.5 on 2024-02-28 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_alter_u_cabinet_yearfoundation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
