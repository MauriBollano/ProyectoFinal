# Generated by Django 4.1.7 on 2023-02-15 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
        migrations.AlterField(
            model_name='recetas',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
    ]
