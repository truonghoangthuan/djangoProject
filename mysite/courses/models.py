from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=1000)
    teacher = models.CharField(max_length=1000)
    excerpt = models.TextField(max_length=3000)
    description = models.TextField()
    num_lessons = models.PositiveSmallIntegerField()
    pictures = models.ImageField(upload_to='courses_pictures')

    def __str__(self):
        return self.name