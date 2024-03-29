# Generated by Django 3.1.6 on 2021-03-28 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Имя')),
                ('phone_number', models.CharField(max_length=70, verbose_name='Номер телефона')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Запрос на отрудничество',
                'verbose_name_plural': 'Запросы отрудничества',
            },
        ),
        migrations.CreateModel(
            name='CourseData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Имя')),
                ('phone_number', models.CharField(max_length=70, verbose_name='Номер телефона')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.avtocourse')),
            ],
            options={
                'verbose_name': 'Запись на курс',
                'verbose_name_plural': 'Записи на курсы',
            },
        ),
    ]
