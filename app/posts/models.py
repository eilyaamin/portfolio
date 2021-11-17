from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=285)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    alt = models.CharField(max_length=20)
    src = models.ImageField(upload_to="images/", default=None)

    def __str__(self):
        return self.alt

class Post(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=285, blank=True, null=True)
    description = models.TextField()
    slug = models.SlugField(verbose_name=_("Post URL"), max_length=255, unique=True)
    tag = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to="images/", default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    deleted_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    author = models.CharField(max_length=128)
    comment = models.CharField(max_length=1024, blank=True, null=True)
    ip_address = models.GenericIPAddressField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    deleted_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.comment

