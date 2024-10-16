from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Course(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False) 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course,
                               related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['title'] 

    def __str__(self):
        return self.title


class Content(models.Model):
    module = models.ForeignKey(Module,
                               related_name='contents',
                               on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE,
                                     limit_choices_to={'model__in': (
                                         'text',
                                         'video',
                                         'image',
                                         'file'
                                     )})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'Content for {self.module.title}' 


class ItemBase(models.Model):
    owner = models.ForeignKey(User,
                              related_name='%(class)s_related',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Text(ItemBase):
    content = models.TextField()

    def __str__(self):
        return f'Text: {self.title}' 


class File(ItemBase):
    file = models.FileField(upload_to='files')

    def __str__(self):
        return f'File: {self.title}'  

class Image(ItemBase):
    file = models.FileField(upload_to='images')

    def __str__(self):
        return f'Image: {self.title}' 

class Video(ItemBase):
    url = models.URLField()

    def __str__(self):
        return f'Video: {self.title}'  
