# Generated by Django 3.1.3 on 2020-11-16 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20201116_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisting',
            name='image',
            field=models.ImageField(blank=True, default='/static/img/default-user.png', null=True, upload_to='media'),
        ),
    ]
