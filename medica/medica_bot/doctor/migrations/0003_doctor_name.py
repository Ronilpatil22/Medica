# Generated by Django 4.1.7 on 2023-04-01 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_remove_doctor_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
