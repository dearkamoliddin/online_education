from django.shortcuts import render
from django.views.generic import TemplateView

from teacher.models import TeacherModel


class TeacherView(TemplateView):
    template_name = 'teachers/teacher.html'
    model = TeacherModel

    def get(self, request, *args, **kwargs):
        teacher = TeacherModel.objects.all()
        context = {'teacher': teacher}
        return render(request, 'teachers/teacher.html', context)
