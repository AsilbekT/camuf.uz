from django.db import models
from django.forms import ValidationError
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from .choices import COUNTRY_CHOICES, SCHOOL_CHOICES, SOCIAL_STATUS, STUDY_LANGUAGES
from django.conf import settings
from urllib.parse import urljoin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.


class UniPhone(models.Model):
    phone = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("University Number")
        verbose_name_plural = _("University Numbers")

class EmailAddress(models.Model):
    email = models.EmailField()

    class Meta:
        verbose_name = _("University email")
        verbose_name_plural = _("University emails")

class UniversityGallery(models.Model):
    image = models.ImageField(upload_to="static/db/unipics/")

    def __str__(self) -> str:
        return _("University pics -> {}").format(self.id)
    
    class Meta:
        verbose_name = _("University picture")
        verbose_name_plural = _("University Pictures")



class Gallery(models.Model):
    image = models.ImageField(upload_to="static/db/gallery/")

    def __str__(self) -> str:
        return _("Gallery -> {}").format(self.id)
    
    class Meta:
        verbose_name = _("Gallery")
        verbose_name_plural = _("Galleries")


class Journal(models.Model):
    name = models.CharField(max_length=200, default="")
    arxiv = models.FileField(upload_to="static/db/journals/")


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _("Journal")
        verbose_name_plural = _("Journals")


class JournalPicture(models.Model):
    image = models.ImageField(upload_to="static/db/journals_images/")


    class Meta:
        verbose_name = _("Journal Image")
        verbose_name_plural = _("Journal Images")


class NewsCatagory(models.Model):
    catagory_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.catagory_name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.catagory_name

    class Meta:
        verbose_name = _("News Category")
        verbose_name_plural = _("News Categories")

class New(models.Model):
    news_catagory = models.ForeignKey(
        NewsCatagory, on_delete=models.CASCADE, blank=True, null=True, related_name='news_catagory')
    title_uz = models.CharField(max_length=200, blank=True, null=True)
    title_en = models.CharField(max_length=200, blank=True, null=True)
    title_ru = models.CharField(max_length=200, blank=True, null=True)
    title_tr = models.CharField(max_length=200, blank=True, null=True)
    subtitle_uz = models.CharField(max_length=200, blank=True, null=True)
    subtitle_ru = models.CharField(max_length=200, blank=True, null=True)
    subtitle_en = models.CharField(max_length=200, blank=True, null=True)
    subtitle_tr = models.CharField(max_length=200, blank=True, null=True)
    body_uz = HTMLField()
    body_ru = HTMLField()
    body_en = HTMLField()
    body_tr = HTMLField()
    date_created = models.DateField()
    image = models.ImageField(upload_to="static/db/news/")
    slug = models.SlugField(blank=True, null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_uz)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title_uz


    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")

class ArticleCatagory(models.Model):
    catagory_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.catagory_name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.catagory_name

    class Meta:
        verbose_name = _("Article Category")
        verbose_name_plural = _("Article Categories")

class Article(models.Model):
    article_catagory = models.ForeignKey(
        ArticleCatagory, on_delete=models.CASCADE, blank=True, null=True, related_name='article_catagory')
    title_uz = models.CharField(max_length=200, blank=True, null=True)
    title_ru = models.CharField(max_length=200, blank=True, null=True)
    title_en = models.CharField(max_length=200, blank=True, null=True)
    title_tr = models.CharField(max_length=200, blank=True, null=True)
    subtitle_uz = models.CharField(max_length=200, blank=True, null=True)
    subtitle_ru = models.CharField(max_length=200, blank=True, null=True)
    subtitle_en = models.CharField(max_length=200, blank=True, null=True)
    subtitle_tr = models.CharField(max_length=200, blank=True, null=True)
    body_en = HTMLField()
    body_ru = HTMLField()
    body_uz = HTMLField()
    body_tr = HTMLField()
    date_created = models.DateField()
    image = models.ImageField(upload_to="static/db/article/")
    slug = models.SlugField(blank=True, null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_uz)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

class Workers(models.Model):
    fullname_uz = models.CharField(max_length=200)
    fullname_en = models.CharField(max_length=200)
    fullname_ru = models.CharField(max_length=200)
    fullname_tr = models.CharField(max_length=200)
    position_uz = models.CharField(max_length=200)
    position_en = models.CharField(max_length=200)
    position_ru = models.CharField(max_length=200)
    position_tr = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    email = models.EmailField()
    telegram = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    about_uz = HTMLField(blank=True, null=True)
    about_en = HTMLField(blank=True, null=True)
    about_ru = HTMLField(blank=True, null=True)
    about_tr = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to="static/db/workers/")
    catagory = models.CharField(max_length=200, default="staff")
    slug = models.SlugField(blank=True, null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname_uz)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.fullname_uz
    
    class Meta:
        verbose_name = _("Worker")
        verbose_name_plural = _("Workers")

class Leaders(models.Model):
    fullname_uz = models.CharField(max_length=200)
    fullname_en = models.CharField(max_length=200)
    fullname_ru = models.CharField(max_length=200)
    fullname_tr = models.CharField(max_length=200)
    position_uz = models.CharField(max_length=200)
    position_en = models.CharField(max_length=200)
    position_ru = models.CharField(max_length=200)
    position_tr = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    email = models.EmailField()
    telegram = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    about_uz = HTMLField(blank=True, null=True)
    about_en = HTMLField(blank=True, null=True)
    about_ru = HTMLField(blank=True, null=True)
    about_tr = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to="static/db/workers/")
    catagory = models.CharField(max_length=200, default="leaders")
    slug = models.SlugField(blank=True, null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname_uz)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.fullname_uz

    class Meta:
        verbose_name = _("Leader")
        verbose_name_plural = _("Leaders")


class Status(models.Model):
    rector = models.ForeignKey(Leaders, on_delete=models.CASCADE, blank=True, null=True)
    percent_of_graduations = models.IntegerField()
    number_of_professors = models.IntegerField()
    number_of_housing = models.IntegerField()
    number_of_students = models.IntegerField()
    about_university_title_uz = HTMLField()
    about_university_title_ru = HTMLField()
    about_university_title_en = HTMLField()
    about_university_title_tr = HTMLField()
    about_university_body_uz = HTMLField()
    about_university_body_ru = HTMLField()
    about_university_body_en = HTMLField()
    about_university_body_tr = HTMLField()
    about_university_image = models.ImageField(
        upload_to="static/db/about_university/")

    university_location = models.CharField(
        max_length=300, blank=True, null=True)
    university_email = models.ManyToManyField(EmailAddress)
    phone_number = models.ManyToManyField(UniPhone)

    def __str__(self):
        return "Universitetni umumiy ma'lumotlari"

    class Meta:
        verbose_name = _("Status")
        verbose_name_plural = _("Statues")



class Event(models.Model):
    in_charge = models.ForeignKey(
        Workers,  on_delete=models.CASCADE, blank=True, null=True)
    title_ru = models.CharField(max_length=200, blank=True, null=True)
    title_en = models.CharField(max_length=200, blank=True, null=True)
    title_tr = models.CharField(max_length=200, blank=True, null=True)
    title_uz = models.CharField(max_length=200, blank=True, null=True)
    subtitle_ru = models.CharField(max_length=200, blank=True, null=True)
    subtitle_uz = models.CharField(max_length=200, blank=True, null=True)
    subtitle_tr = models.CharField(max_length=200, blank=True, null=True)
    subtitle_en = models.CharField(max_length=200, blank=True, null=True)
    body_uz = HTMLField()
    body_ru = HTMLField()
    body_tr = HTMLField()
    body_en = HTMLField()
    date_created = models.DateTimeField()
    image = models.ImageField(upload_to="static/db/news/")
    slug = models.SlugField(blank=True, null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_uz)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

class UndergraduateCourse(models.Model):
    image = models.ImageField(upload_to="static/db/news/")
    title_uz = models.CharField(max_length=200, blank=True, null=True)
    title_en = models.CharField(max_length=200, blank=True, null=True)
    title_ru = models.CharField(max_length=200, blank=True, null=True)
    title_tr = models.CharField(max_length=200, blank=True, null=True)
    subtitle_uz = models.CharField(max_length=200, blank=True, null=True)
    subtitle_ru = models.CharField(max_length=200, blank=True, null=True)
    subtitle_en = models.CharField(max_length=200, blank=True, null=True)
    subtitle_tr = models.CharField(max_length=200, blank=True, null=True)
    course_type = models.CharField(max_length=200, blank=True, null=True)
    body_en = HTMLField(blank=True, null=True)
    body_ru = HTMLField(blank=True, null=True)
    body_tr = HTMLField(blank=True, null=True)
    body_uz = HTMLField(blank=True, null=True)
    duration = models.IntegerField()
    catagory = models.CharField(max_length=200, default="undergraduate")
    slug = models.SlugField(blank=True, null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_uz)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name = _("Undergraduate Course")
        verbose_name_plural = _("Undergraduate Courses")

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
            self.slug = slugify(self.title_uz)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title_uz
    
    class Meta:
        verbose_name = _("Graduate Course")
        verbose_name_plural = _("Graduate Courses")

class InterestedPeople(models.Model):
    saved_email = models.EmailField()

    def __str__(self) -> str:
        return self.saved_email

    class Meta:
        verbose_name = _("Interested People")
        verbose_name_plural = _("Interested People")


class AppliedStudents(models.Model):
    program = models.ForeignKey(UndergraduateCourse, on_delete=models.CASCADE, blank=True, null=True, related_name='program')
    language = models.CharField(max_length=200, choices=STUDY_LANGUAGES, blank=True, null=True)
    surname = models.CharField(max_length=200)
    bot_id = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200)
    fathers_name = models.CharField(max_length=200)
    passport_number = models.CharField(max_length=200)
    passport_pdf = models.FileField(upload_to="static/users/passports")
    country = models.CharField(max_length=200, choices=COUNTRY_CHOICES)
    region = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    schooling = models.CharField(max_length=200, choices=SCHOOL_CHOICES)
    diploma = models.FileField(upload_to="static/users/diplomas")
    social_status = models.CharField(max_length=200, choices=SOCIAL_STATUS)
    social_status_file = models.FileField(upload_to="static/users/social_statuses", null=True, blank=True)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField()
    date_created = models.DateTimeField(default=timezone.now)
    accepted = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.surname  + ", " + self.name
    
    def get_passport_pdf_url(self):
        if self.passport_pdf:
            return urljoin(settings.MEDIA_URL, self.passport_pdf.name)
        return None

    def get_diploma_url(self):
        if self.diploma:
            return urljoin(settings.MEDIA_URL, self.diploma.name)
        return None

    def get_social_status_file_url(self):
        if self.social_status_file:
            return urljoin(settings.MEDIA_URL, self.social_status_file.name)
        return None
    
    @classmethod
    def get_applications_count(cls, start_date=None, end_date=None):
        queryset = cls.objects.all()

        if start_date:
            queryset = queryset.filter(date_created__date__gte=start_date)

        if end_date:
            queryset = queryset.filter(date_created__date__lte=end_date)

        return queryset.count()
    
    def clean(self):
        # Check if the user has already submitted an application
        if self.pk:
            raise ValidationError("Siz allaqachon ariza topshirgansiz.")

        # Check if the passport PDF field is provided
        if not self.passport_pdf:
            raise ValidationError("Skanerlangan pasport yoki identifikatorni yuklang.")

        # Check if the uploaded file is a PDF
        if self.passport_pdf and not self.passport_pdf.name.endswith('.pdf'):
            raise ValidationError("Pasport uchun faqat PDF-fayllarga ruxsat beriladi.")

        # Check if the diploma field is provided
        if not self.diploma:
            raise ValidationError("Diplom yoki taʼlim sertifikatingizni yuklang.")

        # Check if the uploaded file is a PDF
        if self.diploma and not self.diploma.name.endswith('.pdf'):
            raise ValidationError("Diplom uchun faqat PDF fayllarga ruxsat beriladi.")

        # Check if there are no other existing applications for the user
        existing_applications = AppliedStudents.objects.filter(
            email=self.email, 
            passport_number=self.passport_number
            )
        
        if existing_applications.exists():
            raise ValidationError("Siz allaqachon ariza topshirgansiz.")
    

    class Meta:
        verbose_name = _("Applied Student")
        verbose_name_plural = _("Applied Students")


@receiver(post_save, sender=ArticleCatagory)
def send_email_to_addresses(sender, instance, created, **kwargs):
    if created:
        subject = 'New Model Created test'
        message = 'A new model instance has been created. and now testing it one more time'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['asilbek20010211@gmail.com']  # Add your desired email addresses here
        send_mail(subject, message, from_email, recipient_list)