# Generated by Django 3.1.6 on 2021-03-28 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_coursedata_feedbackdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedata',
            name='is_viewed',
            field=models.BooleanField(default=False, verbose_name='Просмотрено'),
        ),
        migrations.AddField(
            model_name='feedbackdata',
            name='is_viewed',
            field=models.BooleanField(default=False, verbose_name='Просмотрено'),
        ),
    ]
