from django.forms import models

from .models import (
    CourseData,
    FeedbackData,
)


class CourseForm(models.ModelForm):
    class Meta:
        model = CourseData
        fields = (
            'course',
            'name',
            'phone_number',
            'message',
        )


class FeedbackForm(models.ModelForm):
    class Meta:
        model = FeedbackData
        fields = (
            'name',
            'phone_number',
            'message',
        )
