from django.contrib import admin

from solo.admin import SingletonModelAdmin

from .models import (
    AvtoSchool, AvtoCourse, Contact, Teacher, CourseData, FeedbackData, Email,
    Slider,
)


@admin.register(AvtoSchool)
class AvtoSchoolAdmin(admin.ModelAdmin):
    list_display = ('title', 'address',)


@admin.register(AvtoCourse)
class AvtoCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'avto_school',)


@admin.register(Contact)
class ContactAdmin(SingletonModelAdmin):
    list_display = ('phone_number', 'email',)


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active')


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone',)


@admin.register(CourseData)
class CourseDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'get_course_title', 'is_viewed')
    exclude = ('is_viewed',)

    def get_course_title(self, obj):
        return obj.course.title

    get_course_title.short_description = 'Курсы'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        CourseData.objects.filter(id=object_id).update(is_viewed=True)
        return super(CourseDataAdmin, self).change_view(request, object_id, form_url, extra_context)


@admin.register(FeedbackData)
class FeedbackDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'is_viewed')
    exclude = ('is_viewed',)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        FeedbackData.objects.filter(id=object_id).update(is_viewed=True)
        return super(FeedbackDataAdmin, self).change_view(request, object_id, form_url, extra_context)
