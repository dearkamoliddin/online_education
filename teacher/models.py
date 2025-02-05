from django.db import models


class TeacherModel(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='media/teachers/', null=True, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
