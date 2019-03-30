# Generated by Django 2.1.7 on 2019-03-29 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190330_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewerysettings',
            name='acceptsReservations',
            field=models.BooleanField(default=True, verbose_name='Accepts reservation'),
        ),
        migrations.AlterField(
            model_name='socialmediasettings',
            name='youtube',
            field=models.URLField(blank=True, help_text='Your YouTube channel or user account URL', max_length=255, null=True, verbose_name='Youtube Url'),
        ),
    ]
