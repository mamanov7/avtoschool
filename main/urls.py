from django.urls import path

from .views import (
    GeneralView, AvtoCourseDetailView, TeacherDetailView, CourseFormView,
    FeedbackFormView, AvtoSchoolDetailView,
)

urlpatterns = [
    path('', GeneralView.as_view(), name="index"),
    path('avtocourse/<int:pk>/', AvtoCourseDetailView.as_view(),
         name="avto_course_detail"),
    path('avtoschool/<int:pk>/', AvtoSchoolDetailView.as_view(),
         name="avto_school_detail"),
    path('teacher/<int:pk>/', TeacherDetailView.as_view(),
         name="teacher_detail"),
    path('feedback-form', FeedbackFormView.as_view(),
         name="feedback_form"),
    path('course-form', CourseFormView.as_view(),
         name="course_form"),
]
