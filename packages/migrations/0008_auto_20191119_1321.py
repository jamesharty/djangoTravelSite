# Generated by Django 2.2.7 on 2019-11-19 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0007_auto_20191119_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='attractions.Attraction'),
        ),
    ]
