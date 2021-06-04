# Generated by Django 3.1.6 on 2021-03-28 12:39

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210327_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Учитель')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('image', models.ImageField(upload_to='teacher/%Y/%m/%d')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учители',
            },
        ),
    ]
