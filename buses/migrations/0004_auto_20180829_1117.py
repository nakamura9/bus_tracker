# Generated by Django 2.1 on 2018-08-29 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0003_auto_20180827_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='trip',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]