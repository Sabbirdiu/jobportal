# Generated by Django 3.1.3 on 2020-11-16 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_applyjob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisting',
            name='image',
            field=models.ImageField(blank=True, default=1, upload_to='media'),
            preserve_default=False,
        ),
    ]
