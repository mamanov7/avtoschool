from django.shortcuts import redirect
from django.views.generic import TemplateView, DetailView, CreateView
from django.contrib import messages

from .forms import (
    CourseForm,
    FeedbackForm,
)
from .models import (
    AvtoSchool,
    AvtoCourse,
    Teacher, Slider,
)
from .utils import (
    prepare_course_data_text_and_notify, prepare_feedback_data_text_and_notify,
)


class GeneralView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(GeneralView, self).get_context_data(**kwargs)
        context['avtoschools'] = AvtoSchool.objects.all()
        context['courses'] = AvtoCourse.objects.all()
        context['teachers'] = Teacher.objects.all()
        context['feedback_data'] = FeedbackForm()
        context['course_data'] = CourseForm()
        context['slider_list'] = Slider.objects.all()

        return context


class AvtoCourseDetailView(DetailView):
    template_name = 'main/avtocourse_detail.html'
    model = AvtoCourse
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super(AvtoCourseDetailView, self).get_context_data(**kwargs)
        context['course_data'] = CourseForm()

        return context


class AvtoSchoolDetailView(DetailView):
    template_name = 'main/avtoschool_detail.html'
    model = AvtoSchool
    context_object_name = 'school'


class TeacherDetailView(DetailView):
    template_name = 'main/teacher_detail.html'
    model = Teacher
    context_object_name = 'teacher'


class CourseFormView(CreateView):
    template_name = 'main/index.html'
    form_class = CourseForm

    def form_valid(self, form):
        course_data = form.save()
        prepare_course_data_text_and_notify(self.request, course_data)
        messages.success(self.request, 'Запись успешно отправлена!')
        return redirect('index')

    def form_invalid(self, form):
        messages.error(self.request, 'Запись не отправлена!')
        return redirect('index')


class FeedbackFormView(CreateView):
    template_name = 'main/index.html'
    form_class = FeedbackForm

    def form_valid(self, form):
        feedback_data = form.save()
        prepare_feedback_data_text_and_notify(self.request, feedback_data)
        messages.success(self.request, 'Заявка успешно отправлена!')
        return redirect('index')

    def form_invalid(self, form):
        messages.error(self.request, 'Заявка не отправлена!')
        return redirect('index')
