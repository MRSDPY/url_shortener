# Generated by Django 3.0.4 on 2020-08-21 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_openurls_activate'),
    ]

    operations = [
        migrations.AddField(
            model_name='openurls',
            name='click',
            field=models.PositiveIntegerField(default=0),
        ),
    ]