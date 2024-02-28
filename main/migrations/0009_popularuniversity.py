# Generated by Django 4.2.5 on 2024-02-27 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_aboutus'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopularUniversity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('rating', models.CharField(max_length=100)),
                ('quality', models.IntegerField()),
                ('price', models.CharField(max_length=100)),
                ('students', models.IntegerField()),
            ],
        ),
    ]
