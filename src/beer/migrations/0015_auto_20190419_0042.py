# Generated by Django 2.1.7 on 2019-04-18 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0014_beeravailability'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beeravailability',
            options={'verbose_name': 'Beer Availability', 'verbose_name_plural': 'Beer Availabilities'},
        ),
        migrations.RemoveField(
            model_name='beer',
            name='availabilities',
        ),
    ]
