# Generated by Django 2.0 on 2017-12-31 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0002_AddTags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='date_time_posted',
            field=models.DateTimeField(auto_now_add=True, verbose_name='posted at'),
        ),
    ]
