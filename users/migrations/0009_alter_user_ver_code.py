# Generated by Django 5.0 on 2023-12-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_ver_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='339651273420', max_length=15, verbose_name='Проверочный код'),
        ),
    ]
