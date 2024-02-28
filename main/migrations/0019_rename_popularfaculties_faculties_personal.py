# Generated by Django 4.2.5 on 2024-02-27 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_students'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PopularFaculties',
            new_name='Faculties',
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('passport', models.URLField()),
                ('degree', models.URLField()),
                ('students', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.students')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.university')),
            ],
        ),
    ]