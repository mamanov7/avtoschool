from django.db import models

from solo.models import SingletonModel
from ckeditor_uploader.fields import RichTextUploadingField


class AvtoSchool(models.Model):
    title = models.CharField(
        max_length=70,
        verbose_name='Название автошколы',
    )
    address = models.CharField(
        max_length=70,
        verbose_name='Адрес автошколы',
    )
    preview_image = models.ImageField(
        upload_to="avto-school/%Y/%m/%d",
        verbose_name="Превью автошколы",
    )
    description = RichTextUploadingField(
        verbose_name='Описание',
    )

    class Meta:
        verbose_name_plural = 'Автошколы'
        verbose_name = 'Автошкола'

    def __str__(self):
        return f'{self.title} {self.address}'


class AvtoCourse(models.Model):
    start_date = models.DateField(verbose_name='Дата начала')
    title = models.CharField(
        max_length=70,
        verbose_name='Название курса',
    )
    description = RichTextUploadingField(
        verbose_name='Описание',
    )
    short_description = models.TextField('Описание для превью')
    avto_school = models.ForeignKey(
        'AvtoSchool',
        on_delete=models.CASCADE,
    )
    preview_image = models.ImageField(
        upload_to="avto-course/%Y/%m/%d",
        verbose_name="Превью курса",
    )

    class Meta:
        verbose_name_plural = 'Курсы'
        verbose_name = 'Курс'

    def __str__(self):
        return f'{self.title} {str(self.avto_school)}'


class Contact(SingletonModel):
    phone_number = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name="Номер телефона",
    )
    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name='Почта',
    )
    address = models.CharField(
        max_length=70,
        blank=True,
        null=True,
        verbose_name='Адрес',
    )

    class Meta:
        verbose_name_plural = 'Контакты'
        verbose_name = 'Контакт'

    def __str__(self):
        return f'{self.phone_number} {self.email}'


class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name='Учитель')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    image = models.ImageField(upload_to='teacher/%Y/%m/%d')
    description = RichTextUploadingField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учители'


class AbstarctFormData(models.Model):
    name = models.CharField(
        max_length=70,
        verbose_name='Имя',
    )
    phone_number = models.CharField(
        max_length=70,
        verbose_name='Номер телефона',
    )
    message = models.TextField(verbose_name='Сообщение')
    is_viewed = models.BooleanField(default=False, verbose_name='Просмотрено')

    class Meta:
        abstract = True


class CourseData(AbstarctFormData):
    course = models.ForeignKey(
        'AvtoCourse',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = 'Записи на курсы'
        verbose_name = 'Запись на курс'

    def __str__(self):
        return f'{self.name} {str(self.course)}'


class FeedbackData(AbstarctFormData):
    class Meta:
        verbose_name_plural = 'Запросы сотрудничества'
        verbose_name = 'Запрос на сотрудничество'

    def __str__(self):
        return f'{self.name} {self.phone_number}'


class Email(models.Model):
    class Meta:
        verbose_name_plural = 'Уведомления - Email'
        verbose_name = 'Уведомления - Email'

    email = models.EmailField(verbose_name='Почта')
    is_active = models.BooleanField(default=True, verbose_name='Активный?')

    def __str__(self):
        return self.email


class Slider(models.Model):
    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'

    text = models.CharField(
        max_length=255, verbose_name='Текст', null=True, blank=True,
    )
    image = models.ImageField(upload_to='teacher/%Y/%m/%d')
    url = models.URLField(verbose_name='Ссылка', null=True, blank=True)

    def __str__(self):
        return self.text or f'N#{self.id} Слайдер'
