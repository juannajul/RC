# Generated by Django 4.1.7 on 2023-03-08 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rc_house', '0002_auto_20230307_0003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='participant',
            options={'ordering': ('-points',), 'verbose_name_plural': 'Participantes'},
        ),
    ]
