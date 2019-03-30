# Generated by Django 2.1.7 on 2019-03-28 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('wagtaildocs', '0010_document_file_hash'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Beer name')),
                ('claim', models.TextField(blank=True, null=True, verbose_name='Beer claim')),
                ('has_polikeg', models.BooleanField(default=False, verbose_name='Polikeg available')),
                ('start_availability', models.DateField(blank=True, null=True, verbose_name='Start availability date')),
                ('end_availability', models.DateField(blank=True, null=True, verbose_name='End availability date')),
                ('tasting_style', models.CharField(max_length=255, null=True, verbose_name='Tasting Style')),
                ('tasting_appearance', models.CharField(max_length=255, null=True, verbose_name='Tasting See')),
                ('tasting_smell', models.CharField(max_length=255, null=True, verbose_name='Tasting Smell')),
                ('tasting_taste', models.CharField(max_length=255, null=True, verbose_name='Tasting Taste')),
                ('tasting_bitter', models.PositiveSmallIntegerField(null=True, verbose_name='Tasting Bitter')),
                ('tasting_sweet', models.PositiveSmallIntegerField(null=True, verbose_name='Tasting Sweet')),
                ('alcoholic_content', models.CharField(max_length=255, verbose_name='ABV')),
                ('ibu', models.CharField(default='15.5', max_length=255, verbose_name='IBU')),
                ('srm', models.SmallIntegerField(default=1, verbose_name='SRM')),
                ('og', models.SmallIntegerField(default=1, verbose_name='OG')),
                ('degree_plato', models.CharField(default='1.0', max_length=10, verbose_name='Degree Plato')),
                ('colour', models.CharField(max_length=255, verbose_name='Colour')),
                ('serving_temperature', models.CharField(max_length=255, verbose_name='Serving Temperature')),
                ('how_to_store', models.CharField(default='Store upright in a dark, cool place. Refrigerate 24 to 48 hours before serving.', max_length=255, verbose_name='How to store Lord Chambray')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('bottle_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('conil_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('glass_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('spec_sheet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
                ('tap_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Beer',
                'verbose_name_plural': 'Beers',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='BeerCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Category name')),
                ('claim', models.TextField(blank=True, null=True, verbose_name='Category claim')),
            ],
            options={
                'verbose_name': 'Beer Category',
                'verbose_name_plural': 'Beer Categories',
                'ordering': ['name'],
            },
        ),
    ]
