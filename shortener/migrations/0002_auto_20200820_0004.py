# Generated by Django 3.0.4 on 2020-08-19 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openurls',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, unique=True),
        ),
        migrations.AlterField(
            model_name='openurls',
            name='shorted_url',
            field=models.CharField(max_length=15),
        ),
    ]
