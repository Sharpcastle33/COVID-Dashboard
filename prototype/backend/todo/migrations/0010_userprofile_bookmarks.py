# Generated by Django 3.1.7 on 2021-05-03 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_auto_20210502_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bookmarks',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
