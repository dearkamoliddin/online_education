from django.db import models

from teacher.models import TeacherModel


class CategoryModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'


class CourseModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    number_of_students = models.IntegerField(default=0)
    price = models.FloatField()
    duration = models.IntegerField()
    teachers = models.ManyToManyField(TeacherModel, blank=True)
    video = models.FileField(upload_to='media/courses')
    category = models.ForeignKey(CategoryModel, related_name='courses', on_delete=models.CASCADE, null=True, blank=True)

    @property
    def duration_of_video(self):
        pass

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Courses'
        verbose_name = 'Course'


class CommentModel(models.Model):
    class RatingChoices(models.TextChoices):
        Zero = '0'
        One = '1'
        Two = '2'
        Three = '3'
        Four = '4'
        Five = '5'

    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    comment = models.TextField()
    rating = models.CharField(max_length=100, choices=RatingChoices.choices, default=RatingChoices.Zero.value)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Comments'
        verbose_name = 'Comment'
