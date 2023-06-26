# Generated by Django 4.2.1 on 2023-06-26 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('rating', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('images', models.ImageField(upload_to='software_images/')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('information', models.TextField()),
                ('features', models.TextField()),
                ('version', models.CharField(max_length=50)),
                ('supported_systems', models.CharField(max_length=255)),
                ('license', models.CharField(max_length=100)),
                ('subscription', models.BooleanField(default=False)),
                ('reviews', models.ManyToManyField(to='catalapp.review')),
                ('tags', models.ManyToManyField(to='catalapp.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Plugin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('images', models.ImageField(upload_to='plugin_images/')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('information', models.TextField()),
                ('features', models.TextField()),
                ('version', models.CharField(max_length=50)),
                ('supported_systems', models.CharField(max_length=255)),
                ('license', models.CharField(max_length=100)),
                ('reviews', models.ManyToManyField(to='catalapp.review')),
            ],
        ),
    ]
