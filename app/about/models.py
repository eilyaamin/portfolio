from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.html import mark_safe
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor_uploader.fields import RichTextUploadingField

# SECTION - MODELS

# ANCHOR - EDUCATION

class Hobby(models.Model):
    name = models.CharField(max_length=54)

    def __str__(self):
        return self.name



# ANCHOR - EDUCATION

class Education(models.Model):
    title = models.CharField(max_length=54)
    institution = models.CharField(max_length=54)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    description = models.CharField(max_length=180)

    def __str__(self):
        return self.title


# ANCHOR - EXPERIENCE

class Experience(models.Model):
    job = models.CharField(max_length=54, verbose_name="Job Title")
    company = models.CharField(max_length=54)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    description = models.CharField(max_length=180)

    def __str__(self):
        return self.job


# ANCHOR - CERTIFICATE

class Certificate(models.Model):
    title = models.CharField(max_length=54)
    date = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.title


# ANCHOR - LANGUAGE
class Language(models.Model):
    language = models.CharField(max_length=54)
    level = models.CharField(max_length=20)

    def __str__(self):
        return self.language


# ANCHOR - SKILL_CATEGORY
class SkillCategory(models.Model):
    title = models.CharField(max_length=54)

    def __str__(self):
        return self.title


# ANCHOR - SKILL
PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

class Skill(models.Model):
    title = models.CharField(max_length=54)
    logo = models.ImageField(upload_to="static/images/", default=None)
    percentage = models.DecimalField(
        max_digits=3, decimal_places=0, default=0, validators=PERCENTAGE_VALIDATOR)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)

    # ANCHOR - DISPLAY LOGO IN ADMIN PANEL
    def SkillLogo(self):
        if self.logo:
            return mark_safe('<img src="{}" height="35" width="35" />'.format(self.logo.url))
        else:
            return ''

    def __str__(self):
        return self.title

# ANCHOR - CV
class Cv(models.Model):
    alt = models.CharField(max_length=54)
    about_me = RichTextUploadingField()
    address = models.CharField(max_length=80)
    photo = models.ImageField(upload_to="static/images/", default=None)
    CV = models.FileField(upload_to="static/cv/", default=None)
    phone = PhoneNumberField()
    email = models.EmailField()
    post_photo = models.ImageField(upload_to="static/images/", default=None)
    homepage_photo = models.ImageField(upload_to="static/images/", default=None)
    homepage_paragraph = RichTextUploadingField()

    def __str__(self):
        return self.alt

    def Photo(self):
        if self.photo:
            return mark_safe('<img src="{}" height="35" width="45" />'.format(self.photo.url))
        else:
            return ''

# ANCHOR - CV
class Job(models.Model):
    title = models.CharField(max_length=500)
    svg = models.ImageField(upload_to="static/images/", default=None)
    description = models.CharField(max_length=100)
    alt = models.CharField(max_length=54)

    def __str__(self):
        return self.title

    def Svg(self):
        if self.svg:
            return mark_safe('<img src="{}" height="35" width="45" />'.format(self.svg.url))
        else:
            return ''