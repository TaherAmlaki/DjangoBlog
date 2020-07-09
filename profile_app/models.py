from django.db import models
from django.contrib.auth.models import User


class ProfileSection(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    route_to = models.CharField(max_length=100)
    order = models.IntegerField()

    def __str__(self):
        return f"{self.title}, {self.order}, {self.route_to}"


class AboutMe(models.Model):
    my_job_title = models.CharField(max_length=100, default="Python Developer")
    short_version = models.TextField(default="Default About Me, short")

    def __str__(self):
        return f"{self.my_job_title}"


class ExperiencesModel(models.Model):
    title = models.TextField()
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(default=None, null=True, blank=True)
    company_icon = models.ImageField(default="default_company.jpg", upload_to="users_pics")
    tasks = models.TextField()
    link_to_company = models.URLField()

    def __str__(self):
        return f"{self.title}@{self.company}"


class EducationModel(models.Model):
    title = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    thesis_title = models.CharField(max_length=100)
    thesis_description = models.TextField()
    university_link = models.URLField()
    university_icon = models.ImageField(default="default_university.jpg", upload_to="user_pics")

    def __str__(self):
        return f"{self.title}@{self.university}"


class CertificatesModel(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    end_date = models.DateField()
    duration = models.CharField(max_length=20)
    certificate_authority = models.CharField(max_length=30)
    certificate_link = models.URLField()
    ca_icon = models.ImageField(default="Udemy.png", upload_to="user_pics")

    def __str__(self):
        return f"{self.title}@{self.certificate_authority}"


class SkillsModel(models.Model):
    title = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    experiences = models.TextField()
    level = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.title}@{self.area}"


class MotivationModel(models.Model):
    job_title = models.CharField(max_length=25)
    job_link = models.URLField(default=None, null=True, blank=True)
    company_name = models.CharField(max_length=25)
    contact_person = models.CharField(max_length=25, default=None, null=True, blank=True)
    contact_person_title = models.CharField(max_length=10)
    company_location = models.CharField(max_length=20, default=None, null=True, blank=True)
    motivation_body = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.job_title}@{self.company_name}"
