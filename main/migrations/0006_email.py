# Generated by Django 3.1.6 on 2021-03-28 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210328_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный?')),
            ],
            options={
                'verbose_name': 'Уведомления - Email',
                'verbose_name_plural': 'Уведомления - Email',
            },
        ),
    ]