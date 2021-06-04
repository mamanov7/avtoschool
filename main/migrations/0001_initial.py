# Generated by Django 3.1.6 on 2021-03-27 14:37

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvtoSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Название автошколы')),
                ('address', models.CharField(max_length=70, verbose_name='Адрес автошколы')),
                ('preview_image', models.ImageField(upload_to='avto-school/%Y/%m/%d', verbose_name='Превью автошколы')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Автошкола',
                'verbose_name_plural': 'Автошколы',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=150, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('address', models.CharField(max_length=70, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='AvtoCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=70, verbose_name='Название курса')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('short_description', models.TextField(verbose_name='Описание для превью')),
                ('preview_image', models.ImageField(upload_to='avto-course/%Y/%m/%d', verbose_name='Превью курса')),
                ('avto_school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.avtoschool')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
                'ordering': ['-created_at'],
            },
        ),
    ]
