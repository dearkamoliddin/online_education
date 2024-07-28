from django.shortcuts import render
from course.models import CategoryModel, CourseModel, CommentModel
from django.views.generic import TemplateView


class CourseView(TemplateView):
    template_name = 'courses/course.html'
    model = CourseModel

    def get(self, request, *args, **kwargs):
        course = CourseModel.objects.all()
        context = {'course': course}
        return render(request, 'courses/course.html', context)
