from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from teacher.views import TeacherView

app_name = 'teacher'

urlpatterns = [
    path('', TeacherView.as_view(), name='teacher'),

]


