# Generated by Django 2.1.3 on 2018-12-01 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='like',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
