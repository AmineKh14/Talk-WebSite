# Generated by Django 2.2.5 on 2019-10-04 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_auto_20190929_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Bio',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]