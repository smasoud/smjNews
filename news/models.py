from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime


def validate_file_extention(value):
    import os
    from django.core.exceptions import ValidationError
    valid_extention = ['.jpg', '.jpeg', '.png']
    ext = os.path.splitext(value.name)[1]
    if not ext.lower() in valid_extention:
        raise ValidationError('Unsupported file extention.')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/user_avarat', null=True, blank=True,
                              validators=[validate_file_extention])
    description = models.CharField(max_length=512, null=False, blank=False)

    def __str__(self):
        return self.user.username + ' | ' + self.user.first_name + ' ' + self.user.last_name


class Articles(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)
    cover = models.FileField(upload_to='files/article_cover', null=False, blank=False,
                             validators=[validate_file_extention])
    content = RichTextField()
    created_at = models.DateTimeField(default=datetime.now(), blank=False)
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    auther = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class category(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)
    cover = models.FileField(upload_to='files/category_cover', null=False, blank=False,
                             validators=[validate_file_extention])

    def __str__(self):
        return self.title
