# Generated by Django 2.2.2 on 2019-06-05 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0002_pumpkin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pumpkin',
            name='city',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='pumpkin',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pumpkin',
            name='origin',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='pumpkin',
            name='pkg',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='pumpkin',
            name='var',
            field=models.CharField(max_length=15),
        ),
    ]