# Generated by Django 3.2 on 2021-04-27 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]
