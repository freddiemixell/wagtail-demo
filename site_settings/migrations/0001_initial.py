# Generated by Django 4.2.1 on 2023-06-08 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, help_text='Enter your facebook  url')),
                ('twitter', models.URLField(blank=True, help_text='Enter your twitter  url')),
                ('youtube', models.URLField(blank=True, help_text='Enter your youtube  url')),
                ('instagram', models.URLField(blank=True, help_text='Enter your instagram  url')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
