# Generated by Django 4.2.1 on 2023-06-30 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalapp', '0008_remove_software_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='subscription',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='catalapp.subscription'),
        ),
    ]
