# Generated by Django 4.2.1 on 2023-07-01 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalapp', '0012_alter_software_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='remaining_days',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
