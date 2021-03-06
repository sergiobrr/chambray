# Generated by Django 2.1.7 on 2019-05-11 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Created at')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Update at')),
                ('sort_order', models.PositiveIntegerField(default=1000, verbose_name='Displaying order')),
                ('sender_full_name', models.CharField(max_length=255, verbose_name='Sender full name')),
                ('sender_email', models.EmailField(max_length=255, verbose_name='Sender email')),
                ('sender_telephone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Sender phone number')),
                ('message_type', models.CharField(choices=[('visit', 'Visit brewery'), ('info', 'Info on beers'), ('business', 'Business occasion')], default='info', max_length=20)),
                ('subject', models.CharField(max_length=255, verbose_name='Message subject')),
                ('body', models.TextField(verbose_name='Message body')),
            ],
            options={
                'verbose_name': 'Contact message',
                'verbose_name_plural': 'Contact messages',
                'ordering': ['-created', 'sender_email'],
            },
        ),
    ]
