# Generated by Django 4.2.1 on 2023-06-27 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalapp', '0002_remove_software_views_software_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='demo_available',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='software',
            name='developer',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='software',
            name='documentation_link',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='software',
            name='download_link',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='software',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='software',
            name='is_new_release',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='software',
            name='is_popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='software',
            name='price',
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.AddField(
            model_name='software',
            name='release_date',
            field=models.DateField(default='2023-02-02'),
        ),
        migrations.AddField(
            model_name='software',
            name='video_link',
            field=models.URLField(default=''),
        ),
    ]
