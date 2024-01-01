from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from taggit.managers import TaggableManager
class PublishedPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
        .filter(status=Post.Status.PUBLISHED)

class PublishedProjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
        .filter(status=Project.Status.PUBLISHED)
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    #author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='blog_posts')
    body = RichTextField()
    thumbnail = models.ImageField(upload_to='images/', default='', blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    tags = TaggableManager()

    objects = models.Manager()  # The default manager.
    published = PublishedPostManager()  # Our custom manager.

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields = ['-publish']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                            self.publish.month,
                            self.publish.day,
                            self.slug])

class Project(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    #author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='blog_posts')
    body = RichTextField()
    thumbnail = models.ImageField(upload_to='images/', default='', blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager()  # The default manager.
    published = PublishedProjectManager()  # Our custom manager.

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields = ['-publish']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:project_detail',
                       args=[self.id])
