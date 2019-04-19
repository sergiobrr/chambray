# Generated by Django 2.1.7 on 2019-04-18 21:07

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0011_auto_20190418_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beercontainer',
            name='beers',
        ),
        migrations.AddField(
            model_name='beer',
            name='availabilities',
            field=modelcluster.fields.ParentalManyToManyField(related_name='beers', to='beer.BeerContainer', verbose_name='Type of containers'),
        ),
    ]
