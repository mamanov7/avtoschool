# Generated by Django 3.1.6 on 2021-03-28 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedbackdata',
            options={'verbose_name': 'Запрос на сотрудничество', 'verbose_name_plural': 'Запросы сотрудничества'},
        ),
    ]
