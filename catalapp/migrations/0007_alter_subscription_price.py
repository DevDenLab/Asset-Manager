# Generated by Django 4.2.1 on 2023-06-30 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalapp', '0006_subscription_is_popular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
