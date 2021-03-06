# Generated by Django 2.2.7 on 2019-11-14 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0004_attraction_ranking'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='image1',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='attraction',
            name='image2',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
