# Generated by Django 4.2 on 2024-01-03 12:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0004_alter_subscription_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='date_create',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='дата выхода урока'),
            preserve_default=False,
        ),
    ]