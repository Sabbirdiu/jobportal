# Generated by Django 3.0.5 on 2020-10-29 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblisting',
            name='qualification',
            field=models.CharField(blank=True, choices=[('Honours', 'Honours'), ('Masters', 'Masters')], max_length=30, null=True),
        ),
    ]
