# Generated by Django 2.2.7 on 2020-03-27 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_blobby__data_qbc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blobby',
            name='_data',
        ),
        migrations.RemoveField(
            model_name='blobby',
            name='_data_qbc',
        ),
        migrations.AddField(
            model_name='blobby',
            name='_data_one',
            field=models.BinaryField(blank=True, db_column='data_one'),
        ),
        migrations.AddField(
            model_name='blobby',
            name='_data_two',
            field=models.BinaryField(blank=True, db_column='data_two'),
        ),
    ]
