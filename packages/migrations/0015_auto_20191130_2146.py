# Generated by Django 2.2.7 on 2019-11-30 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0014_auto_20191130_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='endDate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='startDate',
            field=models.DateField(blank=True),
        ),
    ]
