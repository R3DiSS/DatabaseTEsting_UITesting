# Generated by Django 4.2.4 on 2023-08-26 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
    ]
