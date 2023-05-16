from django.db import models
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField
# Create your models here.


class UniPhone(models.Model):
    phone = models.CharField(max_length=100)


class EmailAddress(models.Model):
    email = models.EmailField()


class Status(models.Model):
    percent_of_graduations = models.IntegerField()
    number_of_professors = models.IntegerField()
    number_of_housing = models.IntegerField()
    number_of_students = models.IntegerField()
    about_university_title = HTMLField()
    about_university_body = HTMLField()
    about_university_image = models.ImageField(
        upload_to="static/db/about_university/")

    university_location = models.CharField(
        max_length=300, blank=True, null=True)
    university_email = models.ManyToManyField(EmailAddress)
    phone_number = models.ManyToManyField(UniPhone)

    def __str__(self):
        return "Universitetni umumiy ma'lumotlari"


class Gallery(models.Model):
    image = models.ImageField(upload_to="static/db/gallery/")

    def __str__(self) -> str:
        return f"Gallery -> {self.id}"


class NewsCatagory(models.Model):
    catagory_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.catagory_name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.catagory_name


class New(models.Model):
    news_catagory = models.ForeignKey(
        NewsCatagory, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    body = HTMLField()
    date_created = models.DateField()
    image = models.ImageField(upload_to="static/db/news/")
    slug = models.SlugField(blank=True, null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Workers(models.Model):
    fullname = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    number = models.CharField(max_length=200, default='')
    email = models.EmailField()
    telegram = models.CharField(max_length=200, default='')
    instagram = models.CharField(max_length=200, default='')
    facebook = models.CharField(max_length=200, default='')
    about = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to="static/db/workers/")
    catagory = models.CharField(max_length=200, default="staff")
    slug = models.SlugField(blank=True, null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.fullname


class Leaders(models.Model):
    fullname = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    number = models.CharField(max_length=200, default='')
    email = models.EmailField()
    telegram = models.CharField(max_length=200, default='')
    instagram = models.CharField(max_length=200, default='')
    facebook = models.CharField(max_length=200, default='')
    about = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to="static/db/workers/")
    catagory = models.CharField(max_length=200, default="leaders")
    slug = models.SlugField(blank=True, null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.fullname


class Event(models.Model):
    in_charge = models.ForeignKey(
        Workers,  on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    body = HTMLField()
    date_created = models.DateTimeField()
    image = models.ImageField(upload_to="static/db/news/")
    slug = models.SlugField(blank=True, null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class UndergraduateCourse(models.Model):
    image = models.ImageField(upload_to="static/db/news/")
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    course_type = models.CharField(max_length=200, blank=True, null=True)
    body = HTMLField(blank=True, null=True)
    duration = models.IntegerField()
    catagory = models.CharField(max_length=200, default="undergraduate")
    slug = models.SlugField(blank=True, null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class GraduateCourse(models.Model):
    image = models.ImageField(upload_to="static/db/news/")
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    course_type = models.CharField(max_length=200, blank=True, null=True)
    body = HTMLField(blank=True, null=True)
    duration = models.IntegerField()
    catagory = models.CharField(max_length=200, default="graduate")
    slug = models.SlugField(blank=True, null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class InterestedPeople(models.Model):
    saved_email = models.EmailField()

    def __str__(self) -> str:
        return self.saved_email
