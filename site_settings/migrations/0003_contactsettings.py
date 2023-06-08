# Generated by Django 4.2.1 on 2023-06-08 11:55

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0002_alter_socialmediasettings_facebook_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', wagtail.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
