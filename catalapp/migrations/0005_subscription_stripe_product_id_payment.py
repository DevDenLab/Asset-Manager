# Generated by Django 4.2.1 on 2023-06-28 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalapp', '0004_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='stripe_product_id',
            field=models.CharField(default='prod_O9kr4qTmAQ036l', max_length=255),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('is_successful', models.BooleanField(default=False)),
                ('software', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalapp.software')),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalapp.subscription')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
