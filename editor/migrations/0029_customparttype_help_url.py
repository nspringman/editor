# Generated by Django 2.0.1 on 2018-01-22 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0028_merge_20180122_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='customparttype',
            name='help_url',
            field=models.URLField(blank=True, verbose_name='URL of documentation'),
        ),
    ]
