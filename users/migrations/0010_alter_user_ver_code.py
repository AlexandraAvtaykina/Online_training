# Generated by Django 4.2 on 2024-01-03 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_ver_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='449614772570', max_length=15, verbose_name='Проверочный код'),
        ),
    ]
